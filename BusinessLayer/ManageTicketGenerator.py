from reportlab.pdfgen import canvas

class ManageTicketGenerator:
    
    # this method generates the pdf ticket
    # @staticmethod
    # def generate_ticket_pdf(flight_details, passenger_list, file_name="Flight_Ticket.pdf"):
    #     c = canvas.Canvas(file_name)
        
    #     # Set title
    #     c.setFont("Helvetica-Bold", 16)
    #     c.drawString(100, 750, "✈ Airline Ticket")
        
    #     # Flight details
    #     c.setFont("Helvetica", 12)
    #     details = [
    #         f"Flight Number: {flight_details['flight_number']}",
    #         f"From: {flight_details['source_city']} → To: {flight_details['destination_city']}",
    #         f"Travel Day: {flight_details['travel_date']} ({flight_details['weekday']})",
    #         f"Departure: {flight_details['start_time']} → Arrival: {flight_details['end_time']}",
    #         f"Distance: {flight_details['distance_km']} km",
    #         f"Fare Amount: ₹{flight_details['fare']}"
    #     ]

    #     y_position = 700
    #     for detail in details:
    #         c.drawString(100, y_position, detail)
    #         y_position -= 30  # Move text down

    #     # Save PDF
    #     c.save()
    #     print(f"🎉 Ticket PDF generated successfully: {file_name}")

    @staticmethod
    def generate_ticket_pdf(flight_details, passenger_list, file_name="Flight_Ticket.pdf"):
        c = canvas.Canvas(file_name)

        # Set title
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, 750, "✈ Airline Ticket")

        # Flight details
        c.setFont("Helvetica", 12)
        details = [
            f"Flight Number: {flight_details['flight_number']}",
            f"From: {flight_details['source_city']} → To: {flight_details['destination_city']}",
            f"Travel Date: {flight_details['travel_date']} ({flight_details['weekday']})",
            f"Departure: {flight_details['start_time']} → Arrival: {flight_details['end_time']}",
            f"Distance: {flight_details['distance_km']} km",
            f"Fare Amount: {flight_details['fare']} INR"
        ]

        y_position = 700
        for detail in details:
            c.drawString(100, y_position, detail)
            y_position -= 30  # Move text down

        # **Adding Passenger Details with Pagination**
        c.setFont("Helvetica-Bold", 14)
        c.drawString(100, y_position - 20, "Passenger Details:")
        y_position -= 50

        c.setFont("Helvetica", 12)
        for idx, passenger in enumerate(passenger_list, 1):
            passenger_info = f"{idx}. Name: {passenger[0]}, Phone: {passenger[1]}, Age: {passenger[2]}, Gender: {passenger[3]}"
            c.drawString(100, y_position, passenger_info)
            y_position -= 25  # Move text down for next passenger

            # **Check if we need a new page**
            if y_position < 50:  # If text reaches bottom margin
                c.showPage()  # Create a new page
                c.setFont("Helvetica", 12)  # Reset font
                y_position = 750  # Reset position for new page

        # Save PDF
        c.save()
        print(f"🎉 Ticket PDF generated successfully: {file_name}")




        

        




    # Example flight details
#     flight_data = {
#         "flight_number": "U167",
#         "source_city": "Mumbai",
#         "destination_city": "Delhi",
#         "travel_date": "07/05/2028",
#         "weekday": "Sunday",
#         "start_time": "18:08",
#         "end_time": "02:44",
#         "distance_km": 1842,
#         "fare": 1842 * 5  # Fare calculation (₹5 per km)
#     }

# ManageTicketGenerator.generate_ticket_pdf(ManageTicketGenerator.flight_data)
