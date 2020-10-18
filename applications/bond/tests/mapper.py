from django.test import TestCase

from applications.bond.mapper import get_mapped_legal_entity

test_legal_entity = [
   {
      "LEI":{
         "$":"353800PGZ4PV86A19K83"
      },
      "Entity":{
         "LegalName":{
            "@xml:lang":"en",
            "$":"MIZKAN EURO LTD."
         },
         "OtherEntityNames":{
            "OtherEntityName":[
               {
                  "@xml:lang":"en",
                  "@type":"ALTERNATIVE_LANGUAGE_LEGAL_NAME",
                  "$":"Mizkan Euro"
               }
            ]
         },
         "LegalAddress":{
            "@xml:lang":"en",
            "FirstAddressLine":{
               "$":"2nd Floor"
            },
            "AdditionalAddressLine":[
               {
                  "$":"Building 10 Chiswick Park"
               },
               {
                  "$":"566 Chiswick High Road"
               }
            ],
            "City":{
               "$":"Chiswick London"
            },
            "Country":{
               "$":"GB"
            },
            "PostalCode":{
               "$":"W4 5XS"
            }
         },
         "HeadquartersAddress":{
            "@xml:lang":"en",
            "FirstAddressLine":{
               "$":"2nd Floor"
            },
            "AdditionalAddressLine":[
               {
                  "$":"Building 10 Chiswick Park"
               },
               {
                  "$":"566 Chiswick High Road"
               }
            ],
            "City":{
               "$":"Chiswick London"
            },
            "Country":{
               "$":"GB"
            },
            "PostalCode":{
               "$":"W4 5XS"
            }
         },
         "OtherAddresses":{
            "OtherAddress":[
               {
                  "@type":"ALTERNATIVE_LANGUAGE_LEGAL_ADDRESS",
                  "@xml:lang":"en",
                  "FirstAddressLine":{
                     "$":"2nd Floor"
                  },
                  "AdditionalAddressLine":[
                     {
                        "$":"Building 10 Chiswick Park"
                     },
                     {
                        "$":"566 Chiswick High Road"
                     }
                  ],
                  "City":{
                     "$":"Chiswick, London"
                  },
                  "Country":{
                     "$":"GB"
                  },
                  "PostalCode":{
                     "$":"W4 5XS"
                  }
               },
               {
                  "@type":"ALTERNATIVE_LANGUAGE_HEADQUARTERS_ADDRESS",
                  "@xml:lang":"en",
                  "FirstAddressLine":{
                     "$":"2nd Floor"
                  },
                  "AdditionalAddressLine":[
                     {
                        "$":"Building 10 Chiswick Park"
                     },
                     {
                        "$":"566 Chiswick High Road"
                     }
                  ],
                  "City":{
                     "$":"Chiswick, London"
                  },
                  "Country":{
                     "$":"GB"
                  },
                  "PostalCode":{
                     "$":"W4 5XS"
                  }
               }
            ]
         },
         "RegistrationAuthority":{
            "RegistrationAuthorityID":{
               "$":"RA000585"
            },
            "RegistrationAuthorityEntityID":{
               "$":"08053234"
            }
         },
         "LegalJurisdiction":{
            "$":"GB"
         },
         "LegalForm":{
            "EntityLegalFormCode":{
               "$":"H0PO"
            }
         },
         "EntityStatus":{
            "$":"ACTIVE"
         }
      },
      "Registration":{
         "InitialRegistrationDate":{
            "$":"2017-12-07T06:00:09+00:00"
         },
         "LastUpdateDate":{
            "$":"2019-12-07T00:00:12+00:00"
         },
         "RegistrationStatus":{
            "$":"ISSUED"
         },
         "NextRenewalDate":{
            "$":"2020-12-07T06:00:09+00:00"
         },
         "ManagingLOU":{
            "$":"353800279ADEFGKNTV65"
         },
         "ValidationSources":{
            "$":"FULLY_CORROBORATED"
         },
         "ValidationAuthority":{
            "ValidationAuthorityID":{
               "$":"RA000585"
            },
            "ValidationAuthorityEntityID":{
               "$":"08053234"
            }
         }
      }
   }
]


class MapJsonToLegalEntity(TestCase):
    """ map json to legal entity """

    def test_get_mapped_legal_entity(self):
        expected = {
            'lei': '353800PGZ4PV86A19K83',
            'legal_name': 'MIZKAN EURO LTD.',
            'status': 'ACTIVE',
            'legal_jurisdiction': 'GB',
            'legal_address': '2nd Floor, Chiswick London W4 5XS, United Kingdom'
        }
        actual = get_mapped_legal_entity(test_legal_entity)
        self.assertEqual(expected, actual)

