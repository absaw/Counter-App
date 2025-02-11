import rumps

class CounterApp(rumps.App):
    def __init__(self):
        super(CounterApp, self).__init__(name="Counter",title="Counter")
        self.menu = [
            rumps.MenuItem(title="Count: 0", callback=None),
            rumps.MenuItem(title="Increment (+)", callback=self.increment),
            rumps.MenuItem(title="Decrement (-)", callback=self.decrement),
            rumps.MenuItem(title="Reset",callback=self.reset_counter),
        ]
      
        self.reset_counter("")
        
    def reset_counter(self, _):
        self.count = 0
        self.update_title()
      
        
    def update_title(self):
        if self.count == 1:
            self.title = f"{self.count} Application Done"
        else:
            self.title = f"{self.count} Applications Done"
        self.menu["Count: 0"].title = f"Count: {self.count}"
        
    def increment(self, _):
        self.count += 1
        self.update_title()

    def decrement(self, _):
        if self.count>0:
            self.count -= 1
            self.update_title()

if __name__ == "__main__":
    CounterApp().run()
