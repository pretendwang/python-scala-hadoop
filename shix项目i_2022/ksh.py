import pandas as pd
import numpy as np
from random import randint
from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline, Page, Pie,Line,WordCloud
from pyecharts.globals import ThemeType
from sqlalchemy import create_engine
#连接数据库
encoding = 'utf8'
engine=create_engine("mysql+pymysql://root:123456@192.168.10.102:3306/computer",echo=True)

# print(df)
# print([df.loc[:,'message'],])

def brand():
    pd.read_sql_table('brand', con=engine)  # 读取数据库表
    df = pd.read_sql_query('select * from brand', con=engine)  # 按照时间从低到高排序
    df_x = df['brand'].values

    df_x1=[i for i in df_x]
    df_y = df['count(brand)'].values
    df_y1=[float(i) for i in df_y]
    # print(df_x1,df_y1)
    bar = (
        Bar(init_opts=opts.InitOpts())
            .add_xaxis(df_x1)
            .add_yaxis('', df_y1)
            .set_series_opts(markline_opts=opts.MarkLineOpts(
            data=[opts.MarkLineItem(type_="max", name="max"), opts.MarkLineItem(type_="min", name="min")]),
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max", name="max"),
                                                    opts.MarkPointItem(type_="min", name="min")]))
            .set_global_opts(
            title_opts=opts.TitleOpts(title='品牌频数图',
                                      pos_left='20%', pos_top='5%'),
            xaxis_opts=opts.AxisOpts(name="品牌", axislabel_opts=opts.LabelOpts(rotate=90),
                                     axispointer_opts=opts.AxisPointerOpts(is_show=True, type_="shadow")),
            tooltip_opts=opts.TooltipOpts(trigger='axis', axis_pointer_type='cross'),
            datazoom_opts=opts.DataZoomOpts(is_show=False, type_='inside', range_start=0),
            legend_opts=opts.LegendOpts(pos_right='5%', pos_top='10%',
                                        textstyle_opts=opts.TextStyleOpts()),
            yaxis_opts=opts.AxisOpts(name="数量", axislabel_opts=opts.LabelOpts(rotate=0),
                                     splitline_opts=opts.SplitLineOpts(is_show=False)))
            .render('brand.html')
    )
brand()

def price():
    pd.read_sql_table('price_count', con=engine)  # 读取数据库表
    df = pd.read_sql_query('select * from price_count', con=engine)  # 按照时间从低到高排序
    df_x = df['price_section'].values
    df_x1 = [i for i in df_x]
    df_y = df['count'].values
    df_y1 = [float(i) for i in df_y]
    c2 = (
        Pie(init_opts=opts.InitOpts())
            .add('', [list(z) for z in zip(df_x1, df_y1)],)
            .set_global_opts(title_opts=opts.TitleOpts(title='价格饼图', pos_left='10%', pos_top='10%'),
                             legend_opts=opts.LegendOpts(is_show=True, pos_left='10%', pos_top='0%'))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True, formatter="{b}: {c}"))
            .render('price.html')
    )
price()
def comment():
    pd.read_sql_table('comment_day_count', con=engine)  # 读取数据库表
    df = pd.read_sql_query('select * from comment_day_count', con=engine)  # 按照时间从低到高排序
    df_x = df['day_section'].values
    df_x1 = [i for i in df_x]
    df_y = df['count(day_section)'].values
    df_y1 = [float(i) for i in df_y]
    # print(df_x1,df_y1)
    line = (
        Line(init_opts=opts.InitOpts())
            .add_xaxis(df_x1)
            .add_yaxis('', df_y1)
            .set_series_opts(markline_opts=opts.MarkLineOpts(
            data=[opts.MarkLineItem(type_="max", name="max"), opts.MarkLineItem(type_="min", name="min")]),
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max", name="max"),
                                                    opts.MarkPointItem(type_="min", name="min")]))
            .set_global_opts(
            title_opts=opts.TitleOpts(title='日评论折线图',
                                      pos_left='20%', pos_top='5%'),
            xaxis_opts=opts.AxisOpts(name="评论区间", axislabel_opts=opts.LabelOpts(rotate=90),
                                     axispointer_opts=opts.AxisPointerOpts(is_show=True, type_="shadow")),
            tooltip_opts=opts.TooltipOpts(trigger='axis', axis_pointer_type='cross'),
            datazoom_opts=opts.DataZoomOpts(is_show=False, type_='inside', range_start=0),
            legend_opts=opts.LegendOpts(pos_right='5%', pos_top='10%',
                                        textstyle_opts=opts.TextStyleOpts()),
            yaxis_opts=opts.AxisOpts(name="数量", axislabel_opts=opts.LabelOpts(rotate=0),
                                     splitline_opts=opts.SplitLineOpts(is_show=False)))
            .render('comment.html')
    )
comment()
def wc():
    pd.read_sql_table('comment_fields', con=engine)  # 读取数据库表
    df = pd.read_sql_query('select * from comment_fields', con=engine)  # 按照时间从低到高排序
    df_x = df['word'].values
    df_x1 = [i for i in df_x]
    df_y = df['count'].values
    df_y1 = [float(i) for i in df_y]
    w1 = (
        WordCloud(init_opts=opts.InitOpts())
            .add("", [list(z) for z in zip(df_x1, df_y1)])
            .set_global_opts(title_opts=opts.TitleOpts(title="评论词云图"))
            .render('wcloud.html')
    )
wc()