# -*- encoding: utf-8 -*-
###############################################################################
# #                                                                           #
# product_feature for Odoo                                                    #
# Copyright (C) 2016 Rubén Cabrera Martínez                                   #
# Copyright (C) 2016 Praxya Soluciones                                        #
# #                                                                           #
# This program is free software: you can redistribute it and/or modify #      #
# it under the terms of the GNU Affero General Public License as #            #
# published by the Free Software Foundation, either version 3 of the #        #
# License, or (at your option) any later version. #                           #
# #                                                                           #
# This program is distributed in the hope that it will be useful, #           #
# but WITHOUT ANY WARRANTY; without even the implied warranty of #            #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the #              #
# GNU Affero General Public License for more details. #                       #
# #                                                                           #
# You should have received a copy of the GNU Affero General Public License #  #
# along with this program. If not, see <http://www.gnu.org/licenses/>. #      #
# #                                                                           #
###############################################################################
###############################################################################
# Product Feature is an Odoo module wich enables Feature management for       #
# products                                                                    #
###############################################################################
{
    'name': 'Product Features',
    'version': '8.0.0.0.1',
    'category': 'Product',
    'summary': 'Add features to products',
    'author': 'Rubén Cabrera Martínez'
              ', Praxya',
    'license': 'AGPL-3',
    'depends': ['product'],
    'data': [
        'views/product_feature_view.xml',
    ],
    'installable': True,
}