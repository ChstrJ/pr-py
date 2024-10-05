class PRFormatter:
    
    def body_mapper(self, tickets, descriptions):
        
        # Add Ticket and Ticket link here
        body = "**JIRA Ticket/Release** \n \n"
        body += self.add_ticket(tickets)
        
        body += "\n"
        
        # Add bullet here
        body += "**Description** \n"
        body += self.add_description(descriptions)
        
        body += "\n"
        
        body += "Refer to the checklist "
        body += "[here](https://qualitytrade.atlassian.net/wiki/spaces/BDT/pages/2708307968/Pull+request+guidelines) \n"
        body += "- [x] Checklist covered"  
        
        return body
        
    def add_ticket(self, tickets):
        format_tickets = []
        
        for ticket in tickets:
            format_tickets.append(f"- {ticket} \n")
            
        return "\n".join(format_tickets) 
    
    def add_description(self, descriptions): 
        format_descriptions = []
        
        for description in descriptions:
            format_descriptions.append(f"- {description} \n")
        
        return "\n".join(format_descriptions)