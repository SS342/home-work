revenue = int(input("выручка:"))
days = int(input('кол-во дней:'))
all_room = int(input('общее колво номеров:'))
sell_room = int(input('колво проданых номеров:'))
load = sell_room / (all_room * days)
load = load * 100 # в процентах
print(load ,'%')
ADR = revenue / (all_room * days * (load / 100))
print(ADR)
RevPav = load / 100 * ADR
print(RevPav)
