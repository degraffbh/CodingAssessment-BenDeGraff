# main.py

import dockingBays as db

# Function to print docking bays information
def print_docking_bays():
    print("Docking Bays:")
    for bay in db.docking_bays:
        print(f"Bay {bay['bay_id']} - Size: {bay['size']}, Schedule: {bay['schedule']}")

# Function to print incoming ships information
def print_incoming_ships():
    print("\nIncoming Ships:")
    for ship in db.incoming_ships:
        print(f"Ship {ship['ship_name']} - Size: {ship['size']}, Arrival: {ship['arrival_time']}, Departure: {ship['departure_time']}")

# Main function
def main():
    print_docking_bays()
    print_incoming_ships()
    
    # TODO: Implement the docking scheduler logic here
    # Levels 1 to 4 and the bonus can be implemented below
    def availableBays():
        scheduleList = []
        idList = []

        for ship in db.incoming_ships: # Loops through all the ships
            for bay in db.docking_bays: # For each ship, loop through all the bays
                timeOverlap = False

                arrivalTime = int(ship['arrival_time'][:2])
                departureTime = int(ship['departure_time'][:2])
                baySchedule = bay["schedule"]

                for time in baySchedule: #Loops through all current scheduled events in the bay
                    startTime = int(time[0][:2])
                    endTime = int(time[1][:2])
                    #Determining if the docking time overlaps with an already scheduled event in the bay
                    timeDifference = (startTime + endTime) - (arrivalTime + departureTime)
                    if timeDifference >= -2 and timeDifference <= 2:
                        timeOverlap = True

                # Checks if the bay and ship size are compadable, times don't overlap, and if the bay isn't taken already
                if bay["size"] == ship["size"] and not timeOverlap and bay["bay_id"] not in idList: 
                    schedule = f"Ship {ship['ship_name']} with size {ship['size']} has been assigned to bay {bay['bay_id']} from {ship['arrival_time']} to {ship['departure_time']}."
                    scheduleList.append(schedule) 
                    idList.append(bay["bay_id"])
        
                    break # Ship stops looknig for a bay once it has one assigned
        
        return scheduleList

    officalSchedule = availableBays()
    print("\nOffical Schedule:")
    for ship in officalSchedule: #Print the officalSchedule
         print(ship)

if __name__ == "__main__":
    main()