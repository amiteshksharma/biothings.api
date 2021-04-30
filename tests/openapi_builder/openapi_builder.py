import sys 
sys.path.insert(1, 'D:/Scripps_Research/biothings.api/')
from biothings.web.openapi import OpenAPIDocumentBuilder
from biothings.web.openapi.contexts import OpenAPIContext, OpenAPIPathItemContext

description = 'The OLS REST API provides access to key biological data from OLS.\
    The services provide a unified interface to query information about ontology terms\
    from GO (the Gene Ontology) and ECO (the Evidence & Conclusion Ontology), Gene\
    Ontology annotations from the EBI''s GOA database, and gene products (proteins\
    from UniProt, RNA from RNAcentral and complexes from ComplexPortal). '

if __name__ == '__main__':
    _base_document = {
        'openapi': '3.0.3',
        'paths': {},
    }

    document = OpenAPIDocumentBuilder()
    document.info()\
            .title('Ontology Lookup Service API')\
            .version('1.0')\
            .description(description)\
            .terms_of_service('https://www.ebi.ac.uk/OLS/services')\
            .contact(name="pharmgkb help desk", email="help@pharmgkb.org", url="https://github.com/newgene")\

    document.server("https://www.ebi.ac.uk/ols/api", "Production server")\

    # unable to do tags

    document.path('/ontologies/doid/children').get().summary('retrieve the children of specified ontology terms')\
    .parameter('id', in_='path', required=True)\
            .type('string')\
    .response_code('200', 'Put Disease Ontology ID here, e.g. DOID:0050686')
    
    print(document)


    
