document.addEventListener('DOMContentLoaded', function () {
    const resumeUploadForm = document.getElementById('resumeUploadForm');
    const resumeFileInput = document.getElementById('resumeFile');
    const autofillForm = document.getElementById('autofillForm');

    resumeUploadForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const formData = new FormData();
        formData.append('resume', resumeFileInput.files[0]);

        // Send the uploaded resume to the Django server for parsing
        fetch('/parse_resume', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            // Validate the extracted data for completeness and accuracy here
            if (data.firstName && data.lastName && data.phone && data.email && data.address && data.formerEmployer && data.position) {
                // Autofill the form fields with parsed data
                autofillForm.elements.firstName.value = data.firstName;
                autofillForm.elements.lastName.value = data.lastName;
                autofillForm.elements.phone.value = data.phone;
                autofillForm.elements.email.value = data.email;
                autofillForm.elements.address.value = data.address;
                autofillForm.elements.formerEmployer.value = data.formerEmployer;
                autofillForm.elements.position.value = data.position;
            } else {
                alert('Invalid or incomplete data extracted from the resume.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            // Handle errors if any
        });
    });
});

