import pycountry


def get_mapped_legal_entity(jsonData):
    found_entity = jsonData[0]
    lei = get_field_value(found_entity['LEI'])

    entity_data = found_entity['Entity']
    legal_name = get_field_value(entity_data['LegalName'])
    legal_jurisdiction = get_field_value(entity_data['LegalJurisdiction'])
    status = get_field_value(entity_data['EntityStatus'])
    legal_address = get_legal_address(entity_data['LegalAddress'])

    legal_entity = {
        'lei': lei,
        'legal_name': legal_name,
        'status': status,
        'legal_jurisdiction': legal_jurisdiction,
        'legal_address': legal_address
    }

    return legal_entity


def get_legal_address(addressData):
    address_line = get_field_value(addressData['FirstAddressLine'])
    city = get_field_value(addressData['City'])
    post_code = get_field_value(addressData['PostalCode'])
    county_alph_2 = get_field_value(addressData['Country'])
    county_name = pycountry.countries.get(alpha_2=county_alph_2).name
    return f'{address_line}, {city} {post_code}, {county_name}'


def get_field_value(field):
    return field['$']

