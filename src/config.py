config = [
    {
        'table_name': 'posts',
        'ignore_columns': ['id', 'created_at', 'updated_at'],
        'substitute_column': {}
    },
    {
        'table_name': 'users',
        'ignore_columns': ['id', 'created_at', 'updated_at'],
        'substitute_column': {
            'user_id': {
                'from': '1',
                'to': '2'
            }
        }
    }
]
