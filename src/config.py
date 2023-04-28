config = [
    {
        'table_name': 'table_name',
        'ignore_columns': ['id', 'created_at', 'updated_at'],
        'substitute_column': {}
    },
    {
        'table_name': 'amenities_master',
        'ignore_columns': ['id', 'created_at', 'updated_at'],
        'substitute_column': {
            'user_id': {
                'from': '1',
                'to': '2'
            }
        }
    }
]
