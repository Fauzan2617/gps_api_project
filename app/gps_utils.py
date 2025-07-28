import datetime


def dmm_to_deg(raw: str, direction: str) -> float:
    """
    Konversi dari DMM (ddmm.mmmm) ke derajat desimal.
    """
    if not raw:
        return 0.0
    # Pisahkan derajat (dua digit pertama) dan menit (sisanya)
    deg = int(raw[:-7])
    minute = float(raw[-7:])
    val = deg + minute / 60
    return -val if direction in ("S", "W") else val


def parse_nmea(line: str) -> dict:
    parts = line.strip().split(",")
    # GGA sentence
    if parts[0].endswith("GGA") and len(parts) > 9:
        # Time (hhmmss), lat, lat_dir, lon, lon_dir, …, altitude, unit
        time_str = parts[1]
        try:
            hh, mm, ss = int(time_str[0:2]), int(time_str[2:4]), int(time_str[4:6])
            iso_time = datetime.datetime.utcnow().replace(
                hour=hh, minute=mm, second=ss, microsecond=0
            ).isoformat() + "Z"
        except Exception:
            iso_time = datetime.datetime.utcnow().isoformat() + "Z"

        lat = dmm_to_deg(parts[2], parts[3])
        lon = dmm_to_deg(parts[4], parts[5])
        altitude = float(parts[9]) if parts[9] else 0.0

        return {
            "time": iso_time,
            "latitude": lat,
            "longitude": lon,
            "altitude": altitude,
        }

    # RMC sentence (status A = valid)
    if parts[0].endswith("RMC") and len(parts) > 8 and parts[2] == "A":
        time_str = parts[1]
        try:
            hh, mm, ss = int(time_str[0:2]), int(time_str[2:4]), int(time_str[4:6])
            iso_time = datetime.datetime.utcnow().replace(
                hour=hh, minute=mm, second=ss, microsecond=0
            ).isoformat() + "Z"
        except Exception:
            iso_time = datetime.datetime.utcnow().isoformat() + "Z"

        lat = dmm_to_deg(parts[3], parts[4])
        lon = dmm_to_deg(parts[5], parts[6])
        speed_kmh = float(parts[7] or 0.0) * 1.852
        heading = float(parts[8] or 0.0)

        return {
            "time": iso_time,
            "latitude": lat,
            "longitude": lon,
            "speed": speed_kmh,
            "heading": heading,
        }



    return {}
