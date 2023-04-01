from fastapi import APIRouter
from neureal.deck import cards
from jinja2 import Environment, FileSystemLoader
from fastapi.responses import HTMLResponse
router = APIRouter()
env = Environment(loader=FileSystemLoader('neureal/templates'))

# get one card
@router.get('/one-card')
def one_card():
	my_deck = cards.get_deck()
	my_card = cards.get_card(my_deck)
	template = env.get_template('one_card.html')
	content = template.render(name = my_card[0]['name'],
								title = my_card[0]['name'],
								rev = my_card[1],
								message = my_card[0]['message'],
								image = my_card[0]['image'],
								url = my_card[0]['url'],
								cardtype = my_card[0]['cardtype'])
	return HTMLResponse(content=content)

# get three cards
@router.get('/three-cards')
def more_cards():
	my_deck = cards.get_deck()
	hand = []
	cards_seen = []
	num = 1
	while num < 4:
		my_card = cards.get_card(my_deck)
		card = my_card[0]["name"]
		if card not in cards_seen:
			cards_seen.append(card)
			hand.append(my_card)
			num +=1
		else:
			num -= 1
	template = env.get_template('three_cards.html')
	content = template.render(hand = hand, title="Three card spread")
	return HTMLResponse(content=content)

# home page
@router.get('/all-cards')
def all_cards():
	template = env.get_template("all_cards.html")
	content = template.render()
	return HTMLResponse(content=content)

# get specific card
@router.get('/one-card/{card_url}')
def specific_card(card_url):
	my_deck = cards.get_deck()
	my_card = list(filter(lambda my_card: my_card['url'] == card_url, my_deck))[0]
	if my_card['sequence'] > 0 :
		previous_card_url = '/one-card/' + list(filter(lambda previous_card: previous_card['sequence'] == (my_card['sequence'] -1), my_deck))[0]['url']
	else :
		previous_card_url = '/all-cards'
	if my_card['sequence'] < 77 :
		next_card_url = '/one-card/' + list(filter(lambda next_card: next_card['sequence'] == (my_card['sequence'] +1), my_deck))[0]['url']
	else :
		next_card_url = '/all-cards'
	template = env.get_template("specific_card.html")
	content = template.render(name = my_card['name'],
								title = my_card['name'],
								message = my_card['message'],
								image = my_card['image'],
							    previous = previous_card_url,
							    next = next_card_url,
							    sequence = my_card['sequence'],
							    cardtype = my_card['cardtype'])
	return HTMLResponse(content=content)
