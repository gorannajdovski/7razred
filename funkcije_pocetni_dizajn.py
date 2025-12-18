# Počinjemo sa dizajnom tkanine koji treba odštampati.
unprinted_designs = ['karirani', 'cvetni', 'leopard']
completed_designs = []
# Štampanje dizajna sve dok dizjani nestanu u listi.
#  Posle svake štampe, dizajn se ubaci u kompletiranu listu.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Odstampan dizajn: {current_design}")
    completed_designs.append(current_design)
# Prikazuje sve odštampane dizajne.
print("\nSledeći dizajni su odštampani:")
for completed_design in completed_designs:
    print(completed_design)



