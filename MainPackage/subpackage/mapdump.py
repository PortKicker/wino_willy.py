
class MapTile():

    def __init__(self , name, description, items):

        self.name = name
        self.description = description
        self.items = items

    def setMovements(self, movements):
        self.movements = movements

    def __str__(self):
        print(f'this is the name of the room: {self.name}')
        print(f'this is {self.description}')

class Player():

    def __init__(self, location):
        self.location = location

    def move(self, direction):
        if self.location.movements[direction]:
            self.location = self.location.movements[direction]
            print( "*** Moved to room " + self.location.name + " ***")
            print( self.location.description )
        else:
            print( "Cannot move that way!" )


court = MapTile('court', 'this is a courthouse', ['pen'])
alano = MapTile('alano club', 'this is the alano club',['flyer'])
skid_row = MapTile('Skid Row', 'this is skid row',[])
disco = MapTile('Defunct Disco','this is a broken down disco',[])
alley = MapTile('alley way','this is an alley way',[])
dooley_st = MapTile('Dooley st.','this is dooley street',[])
bus_stop = MapTile('bus stop','this is a bus stop',[])
town_square = MapTile('town square','this is the town square',[])
mini_mart = MapTile('mini mart', 'this is a mini mart',[])


court.setMovements({"south":town_square})
town_square.setMovements({"north":court, "east":dooley_st})
dooley_st.setMovements({"north":alley,"west":town_square,"east": bus_stop})
bus_stop.setMovements({"north":mini_mart,"west":dooley_st})
mini_mart.setMovements({"south":bus_stop})
alley.setMovements({"north":skid_row,"south":dooley_st})
skid_row.setMovements({"east":disco,"west":alano,"south":alley})
disco.setMovements({"west":skid_row})
alano.setMovements({"east":skid_row})

willy = Player(court)

while True:

    print(willy.location.name)
    print(willy.location.description)
    opt = input('> ').lower()
    willy.move(opt)





         ####### MAP #######

      #     a1    a2   a3
      #      _____________
      #      |   |   |   | a3
      #      |___|___|___|
      #      |   |   |   | b3
      #      |___|___|___|
      #      |   |   |   | c3
      #      |___|___|___|
