{
'name' : 'Sale Module',
    'version' : '15.0.0',
    'summary' : 'sale.module',
    'description' : ' ',
    'category' : ' ',
    'depends' :  ['product'],
    'data' : [ 'security/ir.model.access.csv',
                'views/saleview.xml',
                'views/sequence.xml',
        
     ],
    'demo' : [ ],
    'installable' : True,
    'auto install' : False,
    'assets' : {},

}