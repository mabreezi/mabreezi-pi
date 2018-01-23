# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import PersonForm, ItemForm, TransactionForm, TradeForm

import requests

#View that crates a new person.participant
def add_person(request):
	if request.method == 'POST':
		form = PersonForm(request.POST)

		if form.is_valid():
			new_person = form.save()
			data=  {
    			"$class": "org.kibaati.Person",
    			"personId": new_person.id,
    			"firstName": new_person.first_name,
    			"lastName": new_person.last_name,
    			"role": new_person.role,
    			"balance": 0
  				}

  			#Post the new person to the blockcahin network
  			#r = requests.post('http://server_name/api/Person', data=data)

  			#return r.status_code

	else:
		form = PersonForm()
		section_name ="Add a Person"

	return render(request, 'hyper/add-person.html', {'form':form, 'section_name':section_name} ) 

# view that creates an item tbefore it can be traded
def add_item(request):
	if request.method == 'POST':
		form = ItemForm(request.POST)

		if form.is_valid():
			new_item = form.save()

			data =   {
    			"$class": "org.kibaati.Item",
    			"itemName": new_item.name,
    			"itemId": new_item.id,
    			"description": new_item.description,
    			"quantity": new_item.quantity,
    			"owner": "resource:org.kibaati.Person#" + str(new_item.owner.id)
  				}
  			#Post the new Item to the blockchain network
  			#r= requests.post('http://server_name/api/Item', data=data)

  			#return r.status_code

	else:
		form = ItemForm()
		section_name ="Add an Item"

	return render(request, 'hyper/add-item.html', {'form':form, 'section_name':section_name} )

#view that transfers money from one person to another
def submit_transaction(request):
	if request.method=='POST':
		form = TransactionForm()

		if form.is_valid():
			cd = form.cleaned_data
			sender = cd['sender']
			recipient = cd['recipient']
			amount = cd['amount']

			data = {
    			"$class": "org.kibaati.Payment",
    			"amount": amount,
    			"sender":"resource:org.kibaati.Person#" + str(sender),
    			"recipient": "resource:org.kibaati.Person#" + str(recipient),
    			}

    		#r= requests.post('http://server_name/api/Payment', data=data)
    		
    		#return r.status_code	

	else:
		form = TransactionForm()
		section_name ="Submit a Transaction"

	return render(request, 'hyper/submit-transaction.html',{'form':form, 'section_name':section_name})

#view that transfers an item from one person to another
def make_trade(request):
	if request.method=='POST':
		form = TradeForm()

		if form.is_valid():
			cd = form.cleaned_data
			sender = cd['sender']
			recipient = cd['recipient']
			item = cd['recipient']

			data = {
    			"$class": "org.kibaati.Payment",
    			"item": "resource:org.kibaati.Item#" + str(item),
    			"newOwner": "resource:org.kibaati.Person#" + str(recipient),
    			}

    		#r= requests.post('http://server_name/api/Payment', data=data)
    		
    		#return r.status_code	

	else:
		form = TradeForm()
		section_name = "Make a Trade"

	return render(request, 'hyper/make-trade.html', {'form':form, 'section_name':section_name})

