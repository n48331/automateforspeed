from django.shortcuts import render, redirect
from django.conf import settings
import os
import html
from bs4 import BeautifulSoup
import aspose.words as aw
from django.http import JsonResponse

html_parser = 'html.parser'
img_placeholder = 'https://cse-janssen.indegene.com/emailbuilder/image-placeholder.png'
def bp(modified_html):
    boiler_plate = f'''
    <mjml>
    <mj-head>
        <mj-html-attributes>
        <mj-selector path=".custom">
            <mj-html-attribute name="id">
            body
            </mj-html-attribute>
        </mj-selector>
        </mj-html-attributes>
        <mj-style>
        u + #body a {{
                    color: inherit !important;
                    text-decoration: none !important;
                    font-size: inherit !important;
                    font-family: inherit !important;
                    font-weight: inherit !important;
                    line-height: inherit !important;
                }}
        </mj-style>
        <mj-attributes>
        <mj-all color="#717171" font-family="Verdana"></mj-all>
        </mj-attributes>
        <mj-style id="id_01">
        a:-webkit-any-link {{
            cursor: auto;
            }}
            img+div {{
                display: none;
            }}
            img.g-img+div {{
                display: none;
            }}
            u {{
                text-decoration: underline!important;
            }}
            .blueLink {{
                color: blue !important;
                text-decoration: underline !important;
            }}
            h1, h2, h3, h4, h5, h6 {{ margin: 0; }}
            span, font {{ display: inline-block; }}
            table, td {{ border-collapse: inherit; }} 
            li {{text-align:-webkit-match-parent; display:list-item;}}
            ul li {{
                margin-left: 0px !important;
            }} 
            ol li {{
                margin-left: 0px !important;
            }}  
            ul li span, ol li span {{
            display: inline !important;
            }}
        
    @media(max-width:555px) {{
    .em_clear {{
        clear: both !important;
        width: 100% !important;
        display: block !important;
    }}    
    .table-full {{
    width: 100% !important;
    }}
    .res1 {{
    width: 100% !important;
    text-align: center !important;
    }}
    .image-width table td {{
    width: 100% !important;
    height: auto !important;
    display: block;
        
    }}
    .mob-left-space {{
    padding-left: 5px !important;     
        }}    
    .hide {{
    display: none !important;
    }}
    }}
    
    @media only screen and (min-width: 351px) and (max-width: 569px) {{
    .em_clear {{
        clear: both !important;
        width: 100% !important;
        display: block !important;
    }}     
    .table-full {{
    width: 100% !important;
    }}
    .res1 {{
    width: 100% !important;
    text-align: center !important;
    }}
    .image-width table td {{
    width: 100% !important;
    height: auto !important;
    display: block; 
    }}
    .hide {{
    display: none !important;
    }}
    @media only screen and (min-width: 320px) and (max-width: 350px) {{
    .em_clear {{
        clear: both !important;
        width: 100% !important;
        display: block !important;
    }}     
    .table-full {{
    width: 100% !important;
    }}
    .res1 {{
    width: 100% !important;
    text-align: center !important;
    }}
    .image-width table td {{
    width: 100% !important;
    height: auto !important;
    display: block;
    }}
    .hide {{
    display: none !important;
    }}
    }}
        </mj-style>
        <mj-style id="sup">
        sup{{
                    line-height: 10px;
                    font-size: 10px;
                    vertical-align:top;
                }}
                sup > font
                    {{
                    font-size: 10px;
                    display: inherit;
                    }}
        </mj-style>
        <mj-style id="sub">
        sub{{
                    line-height: 0;
                    font-size: 8px;
                    vertical-align:bottom;
                }}
                sub > font
                    {{
                    font-size: 8px;
                    display: inherit;
                    }}
        </mj-style>
        <mj-raw>
        <!--[if gte mso 9]>
                        <style>
                        li {{
                            text-indent: -1em; 
                        }}
                        </style>
                    <![endif]-->
        </mj-raw>
        <mj-preview>
        &zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
        &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
        &zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
        &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
        &zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
        &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
        &zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
        &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
        &zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
        &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
        &zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
        &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
        &zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
        &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
        &zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
        &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
        &zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
        &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
        &zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
        &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
        &zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
        &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
        &zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
        &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
        &zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
        &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
        &zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
        &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
        &zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;
        &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
        &zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
        </mj-preview>
    </mj-head>
    <mj-body background-color="#f4f4f4" width="600px">
        <mj-wrapper background-color="#ffffff" padding="0px">
    {modified_html}
        </mj-wrapper>
    </mj-body>
    </mjml>
    '''
    return boiler_plate


def remove_elements_from_div(html):
        soup = BeautifulSoup(html, html_parser)
        parent_div = soup.find('div')
        if parent_div:
            first_child_div = parent_div.find('div')
            last_child_div = parent_div.find_all('div')[-1]
            span_elements = parent_div.find_all('span')
            a_tags = parent_div.find_all('a', {'name': True})
            img_tags = parent_div.find_all('img')

            for a_tag in a_tags:
                a_tag.extract()
            for span in span_elements:
                img_element = span.find('img')
                if img_element and 'Document.002.png' in img_element.get('src', ''):
                    span.extract()
            if first_child_div:
                first_child_div.extract()
            if last_child_div:
                last_child_div.extract()
            p_elements = parent_div.find_all('p')
            if p_elements:
                first_child_p = p_elements[0]
                first_child_p.extract()
            for img in img_tags:
                if 'width' in img.attrs:
                    del img['width']
                if 'height' in img.attrs:
                    del img['height']
        return str(soup)

def remove_styles_except_color(html):
        soup = BeautifulSoup(html, html_parser)
        tags_with_style = soup.find_all(lambda tag: tag.has_attr('style'))
        for tag in tags_with_style:
            style_attr = tag['style']
            properties = [prop.strip() for prop in style_attr.split(';')]
            filtered_properties = [prop for prop in properties if prop.startswith(
                ('color', 'background-color', 'font-weight'))]
            tag['style'] = '; '.join(filtered_properties)
            if not tag['style']:
                del tag['style']
        return str(soup)

def convert2mjml(htmlc):
    soup = BeautifulSoup(htmlc, html_parser)
    empty_tags = soup.find_all(lambda tag: tag.name and not tag.contents and tag.name != 'img')

    for empty_tag in empty_tags:
        empty_tag.extract()

    p_tags = soup.find_all('p')
    for p_tag in p_tags:
        img_tags = p_tag.find_all('img')

        for img_tag in img_tags.copy():
            parent_tag = img_tag.parent
            if parent_tag is not None:
                if parent_tag.name != 'p':
                    mj_image_tag = soup.new_tag('mj-image')
                    mj_image_tag['href'] = '#'
                    mj_image_tag['padding'] = '0px'
                    mj_image_tag['src'] = img_placeholder
                    mj_image_tag.string = ''
                    mj_col_tag = soup.new_tag('mj-column')
                    mj_col_tag.append(mj_image_tag)
                elif parent_tag.name == 'p' :
                    mj_image_tag = soup.new_tag('mj-image')
                    mj_image_tag['href'] = '#'
                    mj_image_tag['padding'] = '0px'
                    mj_image_tag['src'] = img_placeholder
                    mj_image_tag.string = ''
                    img_tag.replace_with(mj_image_tag)
                    mj_images = p_tag.find_all('mj-image')
                    for mj_image in mj_images:
                        if mj_image.parent.name == 'p':
                            mj_col_tag = soup.new_tag('mj-column')
                            mj_image.wrap(mj_col_tag)

    return str(soup)

def cleaned_data(html_file_path):

    with open(html_file_path, 'r', encoding='utf-8') as file:
        htmlc = file.read()
    code = convert2mjml(htmlc)
    soup = BeautifulSoup(code, html_parser)
    span_tags = soup.find_all('span')
    for span_tag in span_tags:
        style_attr = span_tag.get('style')
        if style_attr:
            style_attr += '; display: inline;'
        else:
            style_attr = 'display: inline;'
        span_tag['style'] = style_attr
    for p_tag in soup.find_all('p'):
        if p_tag.parent != 'p':
            p_tag.name = 'mj-section'
        if not p_tag.find('mj-column'):
            mj_col_tag = soup.new_tag('mj-column')
            inner_html = html.unescape(p_tag.decode_contents())
            mj_col_tag.append(BeautifulSoup(inner_html, html_parser))
            p_tag.contents = [mj_col_tag]
        empty_span_tags = soup.find_all('span', text=' ',attrs={'style': None})
        for span_tag in empty_span_tags:
            if span_tag.parent.name =='mj-column':
                span_tag.name ='mj-spacer'
                span_tag['height'] = '5px'
                span_tag['padding'] = '0px'
            

        for section_tag in soup.findAll('mj-section'):
            section_tag['padding-left'] = '20px'
            section_tag['padding-right'] = '20px'
            section_tag['padding-top'] = '0px'
            section_tag['padding-bottom'] = '10px'
    spacers = soup.findAll('mj-spacer')
    for spacer in spacers:
        print(spacer.parent.name =='mj-section')
        if spacer.parent.name =='mj-section':
            mj_col_tag = soup.new_tag('mj-column')
            spacer.wrap(mj_col_tag)

    # print(soup.prettify())
    div_tag = soup.find('div')
    div_inner_html = div_tag.encode_contents()
    new_soup = BeautifulSoup(div_inner_html, html_parser)
    img_tags = new_soup.findAll('img')
    for img_tag in img_tags:
        mj_image_tag = new_soup.new_tag('mj-image')
        mj_image_tag['href'] = '#'
        mj_image_tag['padding'] = '0px'
        mj_image_tag['src'] = img_placeholder
        mj_image_tag.string = ''
        img_tag.parent.replace_with(mj_image_tag)

    for mj_column_tag in new_soup.find_all('mj-column'):
        if all(tag.name == 'span' for tag in mj_column_tag.contents):
            mj_text_tag = soup.new_tag('mj-text')
            mj_text_tag['font-size'] = '14px'
            mj_text_tag['line-height'] = '18px'
            mj_text_tag['padding'] = '0px'
            inner_html = html.unescape(mj_column_tag.decode_contents())
            mj_text_tag.append(BeautifulSoup(inner_html, html_parser))
            mj_column_tag.contents = [mj_text_tag]
        

    return new_soup.prettify()



def upload(request):
    for filename in os.listdir(os.path.join(settings.MEDIA_ROOT)):
                if filename.endswith('.html'):
                    file_path = os.path.join(os.path.join(settings.MEDIA_ROOT), filename)
                    os.remove(file_path)
                    print(f"Deleted: {filename}")
    if request.method == 'POST':
        if 'pdf_file' in request.FILES:
            pdf_file = request.FILES['pdf_file']
            pdf_file_path = os.path.join(settings.MEDIA_ROOT, pdf_file.name)
            with open(pdf_file_path, 'wb') as f:
                for chunk in pdf_file.chunks():
                    f.write(chunk)
            html_file_path = pdf_file_path + '.html'
            doc = aw.Document(pdf_file_path)
            doc.save(html_file_path)
            with open(html_file_path, 'r', encoding='utf-8') as file:
                html = file.read()

            cleaned_html = remove_elements_from_div(html)
            cleaned_html = remove_styles_except_color(cleaned_html)


            with open(html_file_path, 'w', encoding='utf-8') as file:
                file.write(cleaned_html)
            current_directory = os.path.join(settings.MEDIA_ROOT)

            # Filter and delete PNG files
            for filename in os.listdir(current_directory):
                if filename.endswith('.png'):
                    file_path = os.path.join(current_directory, filename)
                    os.remove(file_path)
                    print(f"Deleted: {filename}")

            print("Cleaned HTML saved to 'Document.html' file.")
            modified_html = cleaned_data(html_file_path)
            mjml = bp(modified_html)
            os.remove(pdf_file_path)
           
            return render(request, 'code.html', {'mjml':mjml})

    return render(request, 'upload.html')

def upload_success(request):
    return render(request, 'upload_success.html')