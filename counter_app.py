import rumps

class CounterApp(rumps.App):
    def __init__(self):
        super(CounterApp, self).__init__(name="Counter",title="0")
        self.count = 0
        self.update_title()
        self.menu = [
            rumps.MenuItem(title="Count: 0", callback=None),
            rumps.MenuItem(title="Increment (+)", callback=self.increment),
            rumps.MenuItem(title="Decrement (-)", callback=self.decrement)
        ]
    def update_title(self):
        if self.count == 1:
            self.title = f"{self.count} Application Done"
        else:
            self.title = f"{self.count} Applications Done"
    def increment(self, _):
        self.count += 1
        self.update_title()
        self.menu["Count: 0"].title = f"Count: {self.count}"

    def decrement(self, _):
        self.count -= 1
        self.update_title()
        self.menu["Count: 0"].title = f"Count: {self.count}"

if __name__ == "__main__":
    CounterApp().run()
