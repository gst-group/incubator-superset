# GST CONFIG

GST_METADATA_DB_URI = 'mysql://root:guanshantech@106.15.35.240/test_superset'
GST_DEFAULT_DBS = {
    'gst-test-db': 'mysql://root:guanshantech@106.15.35.240/dwiformmaster',
    'gst-test-db2': 'mysql://root:guanshantech@106.15.35.240/dbiformmaster',
}
GST_DEFAULT_TABLES = [
    'gst-test-db.address',
    'gst-test-db.answer',
    'gst-test-db2.chart',
    'gst-test-db2.company',
]