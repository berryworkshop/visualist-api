from .etc import dates_schema

# type
        # title

        # contributor
        #   type
        #     author
        #     editor
        #     translator
        #   name_first
        #   name_last

        # journal
        # issue
        # volume

        # id
        #   value
        #   type
        #     ISBN
        #     ISSN
        #     DOI

        # publication
        #   edition
        #   date
        #   publisher
        #   place

        # archive
        #   name
        #   place

        # online_source
        #   name
        #   URL
        #   accessed

        # newspaper
        #   section

        # abstract
        # note

relation_schema = {
  'dates': {
    'type': 'list',
    'schema': dates_schema
  },
  'section': {
    'type': 'string',
  },
  'pages': {
    'type': 'string',
  }
}
