def show_summary(data):
    print("\n📤 Mengirim Data GPS:")
    print(f" ⏰ Waktu     : {data.get('time', '-')}")
    print(f" 🧭 Latitude  : {data.get('latitude', '-')}")
    print(f" 🧭 Longitude : {data.get('longitude', '-')}")
    print(f" 🏔️ Altitude  : {data.get('altitude', '-')} m")
    print(f" 🚗 Kecepatan : {data.get('speed', '-')} km/h")
    print(f" 🧭 Heading   : {data.get('heading', '-')}°")
