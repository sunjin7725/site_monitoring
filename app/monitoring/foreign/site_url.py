from datetime import datetime


url_dict = {
    'HK00': f'https://www.customs.gov.hk/en/publication_press/press/index_year_{datetime.now().year}.html',
    'IN10': 'https://www.dgft.gov.in/CP/',
    'IN00': 'https://www.indiantradeportal.in/alerts_implemented_spstbt.jsp?lang=0',
    'ID00': 'https://www.beacukai.go.id/berita.html',
    'PH00': 'https://customs.gov.ph/category/news/',
    'US01': 'https://www.cbp.gov/trade/rulings/bulletin-decisions',
    'US00': 'https://www.cbp.gov/newsroom/media-releases/all',
    'VN10': 'https://english.haiquanonline.com.vn/regulations',
    'VN11': 'https://english.haiquanonline.com.vn/world-customs',
    'VN00': 'https://www.customs.gov.vn/index.jsp?pageId=4&cid=25',
    'VN01': 'https://www.customs.gov.vn/index.jsp?pageId=4&cid=26',
}
