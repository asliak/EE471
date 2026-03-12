class MediaItem(object):
    def __init__(self, title, author, is_available = True):
        self.title = title
        self.author = author
        self.is_available = is_available

    def checkout(self):
        if self.is_available == True:
            self.is_available = False
            return "Successful Checkout!"
        
        else:
            return "Already Out!"
    
    def return_item(self):
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Checked Out"
        return f"{self.title} by {self.author} [{status}]"
    
class Book(MediaItem):
    def __init__(self, title, author, page_count, is_available = True):
        super().__init__(title, author, is_available)
        self.page_count = page_count
    
    def __str__(self):
        status = "Available" if self.is_available else "Checked Out"
        return f"{self.title} by {self.author} {self.page_count} pages [{status}]"

class DVD(MediaItem):
    def __init__(self, title, author, duration, is_available=True):
        super().__init__(title, author, is_available)
        self.duration = duration
        
    def checkout(self):
        response = super().checkout()
        if response == "Successful Checkout!":
            return f"{response} Handle with care: Do not scratch the disc."
        return response
    
# We're using super() because we have to inherit the variables from the parent
# class MediaItem. So if any changes happen in the MediaItem.checkout() logically,
# we can still use it as the way it changed in the children class, DVD.

class LibraryCollection(object):
    def __init__(self):
        self.collection = []

    def add_item(self, item):
        self.collection.append(item)
    
    def list_available(self):
        print("Available Objects:")
        for item in self.collection:
            if item.is_available:
                print(item)
