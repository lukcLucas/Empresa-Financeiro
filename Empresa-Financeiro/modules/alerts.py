def set_price_alert(asset, threshold):
    current_price = 120  # preço fictício
    if current_price < threshold:
        print(f"Alert: {asset} price dropped below ${threshold}!")

def send_notification(message):
    print(f"Notification: {message}")
