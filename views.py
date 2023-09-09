import PyPDF2
from django.http import JsonResponse

def parse_resume(request):
    # Check if a file was uploaded
    if 'resume' in request.FILES:
        resume = request.FILES['resume']
        
        # Initialize variables to store extracted data
        first_name = ''
        last_name = ''
        phone = ''
        email = ''
        address = ''
        former_employer = ''
        position = ''

        # PDF parsing (example, you can extend this for other formats)
        if resume.name.endswith('.pdf'):
            pdf = PyPDF2.PdfFileReader(resume)
            text = ''
            for page_num in range(pdf.getNumPages()):
                text += pdf.getPage(page_num).extractText()

            # Implement your logic to extract data from the text
            # You might use regular expressions or other methods here
            
            # Example: Extracting phone number
            phone_match = re.search(r'Phone:\s*(\d{3}-\d{3}-\d{4})', text)
            if phone_match:
                phone = phone_match.group(1)

            # Extract other data similarly
            
        # Prepare the extracted data as a dictionary
        extracted_data = {
            'firstName': first_name,
            'lastName': last_name,
            'phone': phone,
            'email': email,
            'address': address,
            'formerEmployer': former_employer,
            'position': position,
        }

        return JsonResponse(extracted_data)

    return JsonResponse({'error': 'No resume file provided'})

