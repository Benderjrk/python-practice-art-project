class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
  def __repr__(self):
    return """
      {artist}.
      "{title}".
      {year}, {medium}.
      {name}, {location}.
      """.format(
        artist = self.artist,
        title = self.title,
        year = self.year,
        medium = self.medium,
        name = self.owner.name,
        location = self.owner.location
      )

class MarketPlace:
  def __init__(self):
    self.listings = []
  
  def add_listing(self, new_listing):
    self.listings.append(new_listing)

  def remove_listing(self, listing):
    if listing in self.listings:
      self.listings.remove(listing)

  def show_listings(self):
    if self.listings:
      for listing in self.listings:
        print(listing)
    else:
      return "No Listings Yet"

veneer = MarketPlace()
# print(veneer.show_listings())

class Client:
  def __init__(self, name, is_museum, location="No Location Given"):
    self.name = name
    self.is_museum = is_museum
    if is_museum == False:
      self.location = "Private Collection"
    else:
      self.location = location

edytta = Client("Edytta Halpirt", False)
moma = Client("The MOMA", True, "New York")

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910, edytta)

print(girl_with_mandolin)

