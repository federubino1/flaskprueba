x = {"fecha": "hoy"}

try:
    if x["fecha"] == "hoy" and x["a"] == "existe":
        print("A")
except:
    print("no crasheo")