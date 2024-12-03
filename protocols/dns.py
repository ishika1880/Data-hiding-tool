import dns.message
import dns.query

def hide_data_dns(domain, data, data_type):
    try:
        if data_type == 'text':
            hidden_data = "Hidden Text: " + data
        elif data_type == 'image':
            hidden_data = "Hidden Image Data: " + data
        else:
            return "Unsupported data type for DNS"

        # Create a DNS query with the hidden data in the additional section
        query = dns.message.make_query(domain, dns.rdatatype.TXT)
        query.additional.append(dns.rrset.from_text(domain, 300, dns.rdataclass.IN, dns.rdatatype.TXT, hidden_data))
        
        # Send the query (for testing purposes, you can use a local DNS server)
        response = dns.query.udp(query, '8.8.8.8')  # Replace with an actual DNS server
        return f"Simulated DNS query with hidden data sent for domain {domain}"
    except Exception as e:
        return f"DNS Error: {str(e)}"
