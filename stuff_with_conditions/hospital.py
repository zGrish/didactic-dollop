# doctor-database
available_doctors = [ 'joe mama', 'imap ussay', 'cruella deville']
# hardcoded names
requested_doctors = ['joe mama', 'sv']

for requested_doctor in requested_doctors:
    if requested_doctor in available_doctors:
        print(f'Dr.{requested_doctor.title()} is available. Please wait until called.')
    else:
        print(f'Dr.{requested_doctor.title()} is unavailable.')
