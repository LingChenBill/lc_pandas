#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/6/14
# @Author: Lingchen
# @Prescription: 对列名排序
import pandas as pd

movie = pd.read_csv('../data/movie.csv')
print(movie.head())

# 打印列索引
print(movie.columns)

disc_core = ['movie_title', 'title_year', 'content_rating', 'genres']
disc_people = ['director_name', 'actor_1_name', 'actor_2_name', 'actor_3_name']
disc_other = ['color', 'country', 'language', 'plot_keywords', 'movie_imdb_link']
cont_fb = ['director_facebook_likes', 'actor_1_facebook_likes',
           'actor_2_facebook_likes', 'actor_3_facebook_likes',
           'cast_total_facebook_likes', 'movie_facebook_likes']
cont_finance = ['budget', 'gross']
cont_num_reviews = ['num_voted_users', 'num_user_for_reviews', 'num_critic_for_reviews']
cont_other = ['imdb_score', 'duration', 'aspect_ratio', 'facenumber_in_poster']

new_col_order = disc_core + disc_people + disc_other \
                + cont_fb + cont_finance + cont_num_reviews + cont_other
# 新的列索引
print(set(new_col_order))
# 判断新的列与旧列索引是否相等
print(set(movie.columns) == set(new_col_order))

# 打印新的列
movie2 = movie[new_col_order]
print(movie2.head())
