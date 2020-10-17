import matplotlib.pyplot as plt
import numpy as np

data = [
    ('Pride and Prejudice', [('collins', 3.8258888079630977),
                             ('amiable', 3.744577971999677),
                             ('attentions', 3.7089153246472986),
                             ('dislike', 3.684106526489123),
                             ('elizabeth', 3.658051257110682),
                             ('admire', 3.6488519185801356),
                             ('eliza', 3.6488519185801356),
                             ('regiment', 3.6488519185801356),
                             ('expectation', 3.637590029942543),
                             ('dine', 3.6250032132299386),
                             ('sisters', 3.61914383303614),
                             ('astonishment', 3.610843044428259),
                             ('daughters', 3.599004214774396),
                             ('tolerable', 3.5947948531196894),
                             ('indifferent', 3.5947948531196894),
                             ('carriage', 3.5889591471893),
                             ('phillips', 3.5859406786046155),
                             ('distressed', 3.576454063052752),
                             ('recollected', 3.576454063052752),
                             ('elizabeths', 3.5697440179063116)]),
    ('Beowulf', [('heroes', 19.702958536783512),
                 ('warriors', 19.547408864124694),
                 ('helmet', 19.210384573363925), ('b', 19.157170211664855),
                 ('translate', 19.157170211664855),
                 ('edges', 18.957616355293343), ('earls', 18.873360282603155),
                 ('1', 18.665960719058063), ('weapons', 18.536335991842385),
                 ('strife', 18.38314313240567), ('jewels', 18.3256958101169),
                 ('combat', 18.199311701081612), ('folk', 18.092882977683473),
                 ('unto', 18.092882977683473), ('bench', 17.974628840574432),
                 ('proposes', 17.974628840574432),
                 ('warrior', 17.693775264940456), ('earl', 17.693775264940456),
                 ('defender', 17.693775264940456),
                 ('grapple', 17.693775264940456)]),
    ('Scarlet Letter', [('hester', 5.460900531700222),
                        ('minister', 5.363528983930854),
                        ('infant', 5.347504782954534),
                        ('scarlet', 5.321119068564955),
                        ('spiritual', 5.310369333072906),
                        ('reverend', 5.284838711279286),
                        ('wilson', 5.27484846796874),
                        ('venerable', 5.252013626116061),
                        ('gleam', 5.224371449136502),
                        ('indian', 5.224371449136502),
                        ('dost', 5.224371449136502),
                        ('sunshine', 5.190225230514695),
                        ('onward', 5.190225230514695),
                        ('ignominy', 5.190225230514695),
                        ('brook', 5.180395258487206),
                        ('official', 5.169950913207996),
                        ('garb', 5.120713285463158),
                        ('individuals', 5.0904132068509504),
                        ('betwixt', 5.0904132068509504),
                        ('professional', 5.0904132068509504)]),
    ('Frankenstein; or, the Modern Prometheus',
     [('geneva', 16.438689622190342), ('landed', 16.258044681287146),
      ('destruction', 15.806432329029173), ('sledge', 15.806432329029173),
      ('ice', 15.668985091385442), ('crimes', 15.51904265031955),
      ('completion', 15.174175035868005), ('winds', 15.174175035868005),
      ('sailed', 15.174175035868005), ('hailed', 15.174175035868005),
      ('requires', 15.174175035868005), ('delirium', 15.174175035868005),
      ('murderer', 14.59055291910385), ('labour', 14.225789096126253),
      ('commence', 14.225789096126253), ('placid', 14.225789096126253),
      ('dashing', 14.225789096126253), ('traversed', 14.225789096126253),
      ('roared', 14.225789096126253), ('frenzy', 14.225789096126253)]),
    ('Anthem', [('colors', 55.3531214953271), ('we”', 55.3531214953271),
                ('fools', 51.89355140186915),
                ('unmentionable', 51.89355140186915),
                ('wires', 49.42242990654206), ('council', 47.56908878504672),
                ('cities', 46.12760124610592), ('ahead', 46.12760124610592),
                ('enslaved', 46.12760124610592),
                ('brothers”', 46.12760124610592),
                ('whirled', 46.12760124610592), ('bushes', 46.12760124610592),
                ('rocks', 46.12760124610592), ('grey', 46.12760124610592),
                ('lit', 46.12760124610592), ('temple', 46.12760124610592),
                ('soft', 43.2446261682243), ('tunic', 41.51484112149533),
                ('men”', 41.51484112149533), ('damned', 41.51484112149533)]),
    ('The Turn of the Screw', [('what”', 10.20959702330806),
                               ('school”', 10.02396798652064),
                               ('strangest', 9.900215295329028),
                               ('flash', 9.74552443133951),
                               ('miles”', 9.74552443133951),
                               ('shes', 9.546636177638705),
                               ('somehow', 9.546636177638705),
                               ('worry', 9.546636177638705),
                               ('bad”', 9.546636177638705),
                               ('seconds', 9.546636177638705),
                               ('challenge', 9.546636177638705),
                               ('charges', 9.546636177638705),
                               ('flushed', 9.281451839370963),
                               ('extraordinarily', 9.281451839370963),
                               ('prodigious', 9.112698169564217),
                               ('attitude', 8.910193765796125),
                               ('nothing”', 8.910193765796125),
                               ('pockets', 8.910193765796125),
                               ('groan', 8.910193765796125),
                               ('inference', 8.910193765796125)]),
    ('Alice’s Adventures in Wonderland', [('duchess', 25.438015393073115),
                                          ('hare', 25.389837333616537),
                                          ('â', 25.363417107462933),
                                          ('mock', 24.85323343001396),
                                          ('cat', 24.517969870547503),
                                          ('jury', 24.46160672141981),
                                          ('pigeon', 24.192797856349255),
                                          ('footman', 23.82624031307124),
                                          ('id', 23.2967683061141),
                                          ('soup', 23.125468539157378),
                                          ('queen', 23.021299761953966),
                                          ('twinkle', 22.932756301331068),
                                          ('pepper', 22.464740866610025),
                                          ('tail', 21.84072028698197),
                                          ('cook', 20.96709147550269),
                                          ('yet”', 20.967091475502688),
                                          ('gardeners', 20.967091475502688),
                                          ('cats', 20.967091475502688),
                                          ('know—”', 20.967091475502688),
                                          ('arches', 20.967091475502688)]),
    ('The Yellow Wallpaper', [('pattern', 72.3776954303378),
                              ('nursery', 63.18687696299331),
                              ('john', 62.70082406327797),
                              ('creeping', 56.868189266693975),
                              ('bedstead', 56.868189266693975),
                              ('shaded', 56.868189266693975),
                              ('shines', 56.868189266693975),
                              ('darling”', 56.868189266693975),
                              ('bars', 56.868189266693975),
                              ('smell', 54.16018025399426),
                              ('daytime', 50.549501570394646),
                              ('laughs', 50.549501570394646),
                              ('personally', 50.549501570394646),
                              ('selfcontrol', 50.549501570394646),
                              ('lame', 50.549501570394646),
                              ('johns', 50.549501570394646),
                              ('creeps', 50.549501570394646),
                              ('climb', 50.549501570394646),
                              ('creep', 46.66107837267198),
                              ('color', 43.328144203195414)]),
    ("A Doll's House", [('mustnt', 18.089918389287984),
                        ('stove', 17.62607432802419),
                        ('opens', 17.359012595781397),
                        ('shawl', 16.97325676031959),
                        ('doctor', 16.80352419271639),
                        ('lawyer', 16.708049623439596),
                        ('childrens', 16.367069018879604),
                        ('darling', 15.912428212799615),
                        ('manager', 15.912428212799615),
                        ('hm', 15.912428212799615),
                        ('narrowminded', 15.912428212799615),
                        ('rank', 15.779030611015665),
                        ('goodbye', 15.623111336203257),
                        ('doll', 15.275931084287631),
                        ('arent', 15.275931084287631),
                        ('upstairs', 15.275931084287631),
                        ('sofa', 14.321185391519654),
                        ('nurse', 14.321185391519652),
                        ('papa', 14.321185391519652),
                        ('lays', 14.321185391519652)]),
    ('The Masque of the Red Death', [('clock', 144.75), ('echoes', 144.75),
                                     ('revel', 144.75),
                                     ('sixth', 128.66666666666669),
                                     ('masked', 128.66666666666669),
                                     ('evolutions', 128.66666666666669),
                                     ('stalked', 128.66666666666669),
                                     ('chime', 128.66666666666669),
                                     ('dagger', 128.66666666666669),
                                     ('carpet', 115.8),
                                     ('courtiers', 110.28571428571429),
                                     ('chambers', 110.28571428571429),
                                     ('princes', 96.5), ('purple', 96.5),
                                     ('pestilence', 96.5),
                                     ('decorations', 96.5), ('eastern', 96.5),
                                     ('dizziness', 96.5), ('profuse', 96.5),
                                     ('dissolution', 96.5)]),
    ('A Modest Proposal', [('shillings', 96.16336376456617),
                           ('rags', 92.72895791583164),
                           ('expence', 92.72895791583164),
                           ('plump', 92.72895791583164),
                           ('fat', 92.72895791583164),
                           ('carcass', 92.72895791583164),
                           ('annum', 82.42574036962816),
                           ('livelihood', 82.42574036962816),
                           ('sustenance', 82.42574036962816),
                           ('nourishment', 82.42574036962816),
                           ('annually', 82.42574036962816),
                           ('commodity', 82.42574036962816),
                           ('nursed', 82.42574036962816),
                           ('roasted', 82.42574036962816),
                           ('females', 82.42574036962816),
                           ('sale', 82.42574036962816),
                           ('salt', 82.42574036962816),
                           ('dublin', 82.42574036962816),
                           ('sterling', 82.42574036962816),
                           ('infants', 74.18316633266532)]),
    ('The Narrative of the Life of Frederick Douglass An American Slave',
     [('slaves', 14.471007242827055), ('plantation', 14.204499814532943),
      ('slave', 14.041852870091727), ('whip', 14.015106483672502),
      ('thomas', 13.139162328442971), ('fugitive', 13.139162328442971),
      ('hopkins', 13.139162328442971), ('subjected', 12.976950447844912),
      ('clothing', 12.774185597097333), ('sandy', 12.774185597097333),
      ('lash', 12.513487931850449), ('brute', 12.513487931850449),
      ('barbarity', 12.513487931850449), ('corn', 12.513487931850449),
      ('trousers', 12.513487931850449), ('hire', 12.513487931850449),
      ('commenced', 12.353058599390828), ('andrew', 12.165891044854606),
      ('grossest', 12.165891044854606), ('colored', 12.165891044854604)])
]


def show_plot():
    for book in data:
        words = [word[0] for word in book[1]]
        frequency = [word[1] for word in book[1]]

        plt.rcdefaults()
        fig, ax = plt.subplots()

        fig.set_size_inches(7, 10.5)

        y_pos = np.arange(len(words))
        ax.barh(y_pos, frequency, align='center')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(words)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('Word frequency in comparison to average book')
        ax.set_title(book[0])

        plt.show()