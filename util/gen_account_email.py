import random

names=['Mary', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Jennifer',
           'Maria', 'Susan', 'Margaret', 'Dorothy', 'Lisa', 'Nancy', 'Karen',
           'Betty', 'Helen', 'Sandra', 'Donna', 'Carol', 'Ruth', 'Sharon',
           'Michelle', 'Laura', 'Sarah', 'Kimberly', 'Deborah', 'Jessica',
           'Shirley', 'Cynthia', 'Angela', 'Melissa', 'Brenda', 'Amy', 'Anna',
           'Rebecca', 'Virginia', 'Kathleen', 'Pamela', 'Martha', 'Debra',
           'Amanda', 'Stephanie', 'Carolyn', 'Christine', 'Marie', 'Janet',
           'Catherine', 'Frances', 'Ann', 'Joyce', 'Diane', 'Alice', 'Julie',
           'Heather', 'Teresa', 'Doris', 'Gloria', 'Evelyn', 'Jean', 'Cheryl',
           'Mildred', 'Katherine', 'Joan', 'Ashley', 'Judith', 'Rose',
           'Janice', 'Kelly', 'Nicole', 'Judy', 'Christina', 'Kathy',
           'Theresa', 'Beverly', 'Denise', 'Tammy', 'Irene', 'Jane', 'Lori',
           'Rachel', 'Marilyn', 'Andrea', 'Kathryn', 'Louise', 'Sara', 'Anne',
           'Jacqueline', 'Wanda', 'Bonnie', 'Julia', 'Ruby', 'Lois', 'Tina',
           'Phyllis', 'Norma', 'Paula', 'Diana', 'Annie', 'Lillian', 'Emily',
           'Robin', 'Peggy', 'Crystal', 'Gladys', 'Rita', 'Dawn', 'Connie',
           'Florence', 'Tracy', 'Edna', 'Tiffany', 'Carmen', 'Rosa', 'Cindy',
           'Grace', 'Wendy', 'Victoria', 'Edith', 'GlennL', 'Jeffery',
           'Travis', 'Jeff', 'Chad', 'Jacob', 'Lee', 'Melvin', 'Alfred',
           'Kyle', 'Francis', 'Bradley', 'Jesus', 'Herbert', 'Frederick',
           'Ray', 'Joe', 'Edwin', 'Don', 'Eddie', 'Ricky', 'Troy', 'Randall',
           'Barry', 'Alexander', 'Bernard', 'Mario', 'Leroy', 'Francisco',
           'Marcus', 'Micheal', 'Theodore', 'Clifford', 'Miguel', 'Oscar',
           'Jay', 'Jim', 'Tom', 'Calvin', 'Alex', 'Jon', 'Ronnie', 'Bill',
           'Lloyd', 'Tommy', 'Leon', 'Derek', 'Warren', 'Darrell', 'Jerome',
           'Floyd', 'Leo', 'Alvin', 'Tim', 'Wesley', 'Gordon', 'Dean']
def gen_account():
    mails_header=['hotmail.com','outlook.com','gmail.com','yahoo.com','yaohoo.co.uk','mail.com','mail.ru','web.de','aol.com',]
    chars = 'abcdefghijklmnopqrstuvwxyz' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + '0123456789'
    pre_name=''.join(random.sample(chars,random.randint(2,5)))
    first_name=random.choice(names)
    last_name=pre_name
    pre_name=[first_name,''.join(random.sample(list('_0123456789_'),random.randint(1,5))),pre_name]
    random.shuffle(pre_name)
    mail="%s%s%s@"%tuple(pre_name)+random.choice(mails_header)
    pwd=mail.split('@')[0]  
    return  mail,pwd,first_name,last_name
print gen_account()
