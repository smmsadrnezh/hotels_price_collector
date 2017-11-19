import csv


def write_html(rooms):
    html = """
<html>
<head>
    <title>Hotel Price Collector</title>
    <link rel="shortcut icon" type="image/png" href="https://www.gt724.com/templates/default/interface/images/favicon.ico">
    <meta charset="utf-8">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
          integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <!-- Optional theme -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css"
          integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
    <style>

        body {
            font-family: 'IranSans';
        }

        h1, h2, h3 {
            font-family: 'IranSans';
            font-weight: normal;
        }

        @font-face {
            font-family: IRANSans;
            font-style: normal;
            font-weight: bold;
            src: url('fonts/eot/IRANSansWeb_Bold.eot');
            src: url('fonts/eot/IRANSansWeb_Bold.eot?#iefix') format('embedded-opentype'),  /* IE6-8 */
                 url('fonts/woff2/IRANSansWeb_Bold.woff2') format('woff2'),  /* FF39+,Chrome36+, Opera24+*/
                 url('fonts/woff/IRANSansWeb_Bold.woff') format('woff'),  /* FF3.6+, IE9, Chrome6+, Saf5.1+*/
                 url('fonts/ttf/IRANSansWeb_Bold.ttf') format('truetype');
        }
        @font-face {
            font-family: IRANSans;
            font-style: normal;
            font-weight: 500;
            src: url('fonts/eot/IRANSansWeb_Medium.eot');
            src: url('fonts/eot/IRANSansWeb_Medium.eot?#iefix') format('embedded-opentype'),  /* IE6-8 */
                 url('fonts/woff2/IRANSansWeb_Medium.woff2') format('woff2'),  /* FF39+,Chrome36+, Opera24+*/
                 url('fonts/woff/IRANSansWeb_Medium.woff') format('woff'),  /* FF3.6+, IE9, Chrome6+, Saf5.1+*/
                 url('fonts/ttf/IRANSansWeb_Medium.ttf') format('truetype');
        }
        @font-face {
            font-family: IRANSans;
            font-style: normal;
            font-weight: 300;
            src: url('fonts/eot/IRANSansWeb_Light.eot');
            src: url('fonts/eot/IRANSansWeb_Light.eot?#iefix') format('embedded-opentype'),  /* IE6-8 */
                 url('fonts/woff2/IRANSansWeb_Light.woff2') format('woff2'),  /* FF39+,Chrome36+, Opera24+*/
                 url('fonts/woff/IRANSansWeb_Light.woff') format('woff'),  /* FF3.6+, IE9, Chrome6+, Saf5.1+*/
                 url('fonts/ttf/IRANSansWeb_Light.ttf') format('truetype');
        }
        @font-face {
            font-family: IRANSans;
            font-style: normal;
            font-weight: 200;
            src: url('fonts/eot/IRANSansWeb_UltraLight.eot');
            src: url('fonts/eot/IRANSansWeb_UltraLight.eot?#iefix') format('embedded-opentype'),  /* IE6-8 */
                 url('fonts/woff2/IRANSansWeb_UltraLight.woff2') format('woff2'),  /* FF39+,Chrome36+, Opera24+*/
                 url('fonts/woff/IRANSansWeb_UltraLight.woff') format('woff'),  /* FF3.6+, IE9, Chrome6+, Saf5.1+*/
                 url('fonts/ttf/IRANSansWeb_UltraLight.ttf') format('truetype');
        }
        @font-face {
            font-family: IRANSans;
            font-style: normal;
            font-weight: normal;
            src: url('fonts/eot/IRANSansWeb.eot');
            src: url('fonts/eot/IRANSansWeb.eot?#iefix') format('embedded-opentype'),  /* IE6-8 */
                 url('fonts/woff2/IRANSansWeb.woff2') format('woff2'),  /* FF39+,Chrome36+, Opera24+*/
                 url('fonts/woff/IRANSansWeb.woff') format('woff'),  /* FF3.6+, IE9, Chrome6+, Saf5.1+*/
                 url('fonts/ttf/IRANSansWeb.ttf') format('truetype');
        }
    </style>
</head>
<body>
<table class="table table-hover">
    <thead>
    <tr>
    <th>نام هتل</th>
    <th>نام اتاق</th>
    <th>نام وبسایت</th>
    <th>قیمت</th>
    <th>تاریخ</th>
    </tr>
    </thead>

    <tbody>
"""

    for room in rooms:
        if (isinstance(room, str)):
            continue

        html += '\n<tr><td>' + room["hotel_name"] + '</td><td>' + room["room_name"] + '</td><td>' + room[
            "website_name"] + '</td><td>' + room["price"] + '</td><td>' + room["date"] + '</td></tr>'

    html += """
    </tbody>
</table>
</body>
"""

    with open('index.html', 'w', newline='') as html_file:
        html_file.write(html)
        html_file.close()


def write_csv(rooms):
    with open('prices.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')

        spamwriter.writerow(["نام هتل", "نام اتاق", "نام وبسایت", "قیمت", "تاریخ"])

        for room in rooms:
            spamwriter.writerow([room["hotel_name"], room["room_name"], room["website_name"], room["price"],
                                 room["date"]])
