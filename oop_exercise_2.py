# Class Aggregation
class Player:
    def __init__(self, name, position, number):
        # Initialize the name, position, and number properties
        self.name = name
        self.position = position
        self.number = number

class Team:
    def __init__(self, name):
        # Initialize the name property and an empty players list
        self.name = name
        self.players = []

    def add_player(self, player):
        # Add a Player instance to the team's players list
        self.players.append(player)

    def get_player_info(self, number):
        # Find the player by number and return formatted player info
        for player in self.players:
            if player.number == number:
                return f"{player.name} ({player.position}) - {player.number}"
        return "Player not found"

# Test your implementation
player1 = Player("John Doe", "Forward", 10)
player2 = Player("Jane Smith", "Midfielder", 8)
player3 = Player("Mark Johnson", "Defender", 4)

team1 = Team("Dream Team")
team1.add_player(player1)
team1.add_player(player2)

# Print player info
print(team1.get_player_info(10))  # Should output "John Doe (Forward) - 10"
print(team1.get_player_info(8))   # Should output "Jane Smith (Midfielder) - 8"
print(team1.get_player_info(4))   # Should output "Player not found"
