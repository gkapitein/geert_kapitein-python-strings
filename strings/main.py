# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# part 1
first_player = 'Ruud Gullit'
second_player = 'Marco van Basten'
goal_0 = 32
goal_1 = 54

scorers = f'{first_player} {goal_0}, {second_player} {goal_1}'
print(scorers)

report = f'{first_player} scored in the {goal_0}nd minute' '\n'f'{second_player} scored in the {goal_1}th minute'
print(report)

# part 2
# player
player = 'Marco van Basten'
print(player)

# first name
first_name = player[:player.find(' ')]
print(first_name)

# last name length
last_name_len = len(player[player.find(' ') + 1:])
print(last_name_len)

# short name
name_short = player[:1] + '.' + player[player.find(' '):]
print(name_short)

# chant
chant = ((first_name + '! ') *
         (len(player[:player.find(' ')]) - 1) + first_name + '!')
print(chant)

# good chant
good_chant = (chant[-1] != ' ')
print(good_chant)
