# Scenario: You are managing a guest list for a high-profile wedding. You have two lists: one for the 
# confirmed guests and another for the waitlisted guests. The couple wants a simple wedding with close friends and family in attendance so there is
# room for only 10 guests. Follow the instructions to manage the guest lists accordingly. Write the program in a file `wedding_guest_manager.py`.


# Currently, Alice, Charlie, Eve, Bob, Frank, Grace, David, Hannah, Liam and Mia have accepted invitations to the wedding and are on the 
# confirmed_guests list. The confirmed_guests list is full. New guests who accept the invitation will be waitlisted.
print("\n\nstage 1")
confirmed_guests = ['Alice', 'Charlie', 'Eve', 'Bob', 'Frank', 'Grace', 'David', 'Hannah', 'Liam', 'Mia']
waitlist = []
print(f'confirmed_guests: {confirmed_guests}')
print(f'waitlist: {waitlist}')
# Three siblings Ken, Jack and Ivy accept the invitation but are put on the waitlist.
waitlist = ['Ken', 'Jack', 'Ivy']
print("\n\nstage 2")
print(f'confirmed_guests: {confirmed_guests}')
print(f'waitlist: {waitlist}')

# Noah, the groom’s ex-classmate in the university and Oliver who lives next door to the bride have accepted the invitation. Put them on the
#  waitlist.
waitlist.extend(['Noah', 'Oliver'])
print("\n\nstage 3")
print(f'confirmed_guests: {confirmed_guests}')
print(f'waitlist: {waitlist}')

# Alice has a family emergency and won’t be able to attend the wedding, She cancels her attendance. Remove Alice from the confirmed guest list 
# and add the first person from the waitlist to the confirmed list.
confirmed_guests.remove('Alice')
confirmed_guests.append(waitlist.pop(0))
print("\n\nstage 4")
print(f'confirmed_guests: {confirmed_guests}')
print(f'waitlist: {waitlist}')

# Charlie is the godfather of the groom and he is the one funding the wedding. Therefore he is a VIP guest and the couple has asked you to make
#  sure he is on the guestlist. Check whether or not Charlie is on the guestlist.
print("\n\nstage 5")
print(f" it is {'Charlie' in confirmed_guests} that Charlie is on the guestlist")

# David and Eve have decided they no longer want to attend the wedding and therefore cancel their attendance. Remove them from the confirmed_guests
#  list.
confirmed_guests.remove('David')
confirmed_guests.remove('Eve')
print("\n\nstage 6")
print(f'confirmed_guests: {confirmed_guests}')
print(f'waitlist: {waitlist}')

# Move the first 2 people on the waitlist into the guestlist to fill up the newly freed slots.
confirmed_guests.append(waitlist.pop(0) )
confirmed_guests.append(waitlist.pop(0) )
print("\n\nstage 7")
print(f'confirmed_guests: {confirmed_guests}')
print(f'waitlist: {waitlist}')

# Oliver just realized the day of the wedding is the same day he has to take his pet to see the vet and he cancels his attendance. Remove him 
# from the waitlist.
waitlist.remove('Oliver')
print("\n\nstage 8")
print(f'confirmed_guests: {confirmed_guests}')
print(f'waitlist: {waitlist}')

# The event planner has asked you for the names of the last 3 guests on the guest list because she needs to make additional arrangements for them.
#  Get her this information.
print("\n\nstage 9")
print(confirmed_guests[-3:])
print(f'confirmed_guests: {confirmed_guests}')
print(f'waitlist: {waitlist}')

# The bride and groom have decided that they want to allow room for 5 more people to attend their wedding. Move waitlisted guest (Noah) into the 
# confirmed_guests list.
confirmed_guests.append(waitlist.pop(0))
print("\n\nstage 10")
print(f'confirmed_guests: {confirmed_guests}')
print(f'waitlist: {waitlist}')

# The event planner wants a report on the number of people who will be attending the wedding. Give her this information.
print("\n\nstage 11")
print(f'Number of confirmed guests: {len(confirmed_guests)} ')
print(waitlist)


# The event planner has also requested that you give her a list of all the names of the confirmed_guests.
# The guests would be seated alphabetically at the venue and so she wants the names in alphabetical order.
confirmed_guests.sort()
print("\n\nstage 12")
print(f'confirmed_guests: {confirmed_guests}')
print(f'waitlist: {waitlist}')

# A new guest called Collins who is the son of Grace and Noah would be attending on their behalf, Replace Grace and Noah on the 
# confirmed_guests list with Collins. Make sure you re-sort the list.
confirmed_guests.remove('Grace',)
confirmed_guests.remove('Noah',)
confirmed_guests.append('Collins')
confirmed_guests.sort()
print("\n\nstage 13")
print(f'confirmed_guests: {confirmed_guests}')
print(f'waitlist: {waitlist}')

# The caterer has also requested for the confirmed_guests list so she can provide the guests with customized bags containing their food with
# their names on it. Give her a copy of the confirmed_guests list titled guests_list_for_caterer`.
guests_list_for_caterer = confirmed_guests.copy()
print("\n\nstage 14")
print(f'guests_list_for_caterer: {guests_list_for_caterer}')
print(f'confirmed_guests: {confirmed_guests}')
print(f'waitlist: {waitlist}')

# The deadline for accepting the invitations sent has now passed. There is no more need for the waitlist. Clear the waitlist
waitlist.clear()
print("\n\nstage 15")
print(f'confirmed_guests: {confirmed_guests}')
print(f'waitlist: {waitlist}')


