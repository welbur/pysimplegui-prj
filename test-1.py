"""
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import remi.gui as gui
from remi import start, App
from threading import Timer


class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)


    def main(self):
        # the margin 0px auto centers the main container
        verticalContainer = gui.Widget(width=320, margin='0px auto', style={'display': 'block', 'overflow': 'hidden'})

 #       horizontalContainer = gui.Widget(width='100%', layout_orientation=gui.Widget.LAYOUT_HORIZONTAL, margin='0px', style={'display': 'block', 'overflow': 'auto'})


        #wwb
        imgurl = r'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAYAAADDPmHLAAAan0lEQVR4Xu1dC5gcVZU+51Z3Og8SIibgI0hk' \
                 'A0l3VXUSQ6IRkPCSlyLy8ANWVlEQFURBRRF0QVxcVllRVtRFRUFwXRRh5aWwCD4IqEPC1K2eSYgQUXklGMwkwzy679nvDzXsZNI9fau6ej' \
                 'I9M+f7+ku+b+67/rp17zn/OYdpQsb1CvC4nv3E5GkCAOMcBBMAmADAOF+BcT79MbsDrFixIrN+/frM1KlTM5MmTcrUes59fX3l7u7u8ty5' \
                 'c8v3339/ebzhYawAwPE8z2XmNxhj8kqpPYnoFSIyE/8S0QwiUlUeriGizUS0iYj+RkQbRWQ9M5eIqF1r3THWAdFSACgUCpOIaLdMJrOrMW' \
                 'YvETlAKbW/iLyZiCY34WH1EdFDIvKAiPzCcZynAJYgCACaShP6G/EmWwUAqlgsHmyMOUdEFjEz3mz8RlKwWzwf/dqJ6Nv5fP6+m2++uaWB' \
                 'MKoBUCwWdxeRw40xpzPzQURU81s+kkiI+hIi+gMR/UhE7po9e/baVjxDjFYAKNd138fMl0ff8NH04IdiDUDowqeCiL6otb5/J4AxcZejCg' \
                 'CLFi2aWS6XTyai04loWeJZ7dyKD0a7wp1hGK7buUOp3/toAQDn8/k3Oo7zYyJ6bf1ht0SJXiL6WrlcvqKzsxNnh1EpOx0Aruvuz8znE9Fb' \
                 'iWiXUblKjQ3qCWa+ulKpXFsqlbY01lT6tXcaAHzfx/38IyJyafrTGpUtrlRKnd/e3v770XSF3CkA8DzvGByYiCg/yk72zUbO34noh9FnYX' \
                 '2zO7Npf0QBsHjx4tn9/f2fJaIPEFHOZoAJykB508XMvSKCOzq0gqNKmBkP/2JmvrW9vX3rzhzciAEgn8+/wXGcbxLR0iZMuIeZfy4idxPR' \
                 'g0qpLmNMmZm/JyKH2PQnIlcw8xQR8ZjZI6Ldbeo1UAZ2h5u01u9poI2GqzYdAFDfMvPJzHwNEU1reMQvNYCtdDUzPywiv5o+ffp9K1eufH' \
                 'FI27APoJxtnwu11tDwbZNisTinXC4vZ+Y3EVGBmfclork1bAqNTOvecrl8Zmdn5075JDQVAMuXL5+yefPma5j53Sl962G0+Y5S6ppyufzX' \
                 'UqnUT0RQxOwgnuf9AxHZ3sM3zZo1a/damjxYFru6uiZ1d3fvrZQ6TSn1jyKS5nV1kzHmkFKptLoRJCWp2zQA5PP5VyulvsHMbyMiJ8ngBt' \
                 'V5ALp3IrpHa/2sTVu+7x8lInfalCWiB7TWKyzLEhRW/f39BzLzO4joMCLay7buMOWgKzhPa31DCm1ZN9EUAEQLdDczv9F6JDsWrDAzHvbH' \
                 'giC4OW47nud9lIiusqz3Na01yseWYrE4zRiDq+yHI4tko2t6kdYaN6SqO1vsAdap0Ohgd2geih2l1HdFBN/MRMLMIRFdycx3tLe3P5ekEd' \
                 'd1v8XMuG3YyBla6+/YFKxVxvf9BSJyWnTDmdVAW1AWfVRr/d0G2rCumioA8vn8XplM5kEReY31CLYvCKPKzVrr9yesP1BNeZ73OyJaYtFO' \
                 '2RhzcKlU+o1F2bpFXNddyMw3EdE8IgJ/IamcoLW+JWll23qpAQATJ6I7mTnRwxeRVSLywb6+vkfXrVsHPXpiKRQKr1JK4VRto2t4npkPCI' \
                 'KgM3GHQyruvffeu06dOvVEIvpyA7wFnAlO1Vr/Iq1xVWsnFQD4vr+3iNxKRH6CwYJd83UR+XIYhqBlNSzFYvEiY8wXLBvqMMYsa4aePlqX' \
                 'fyOio4hoquV4BheDMusdYRj+PEFdqyoNA8DzvD2Y+X9FxLXqcftCz1YqlXd3dHT8Mi39eHT1fJyZX2UzHmb+VhAEH7Qpm6TM3LlzJ0+bNm' \
                 '0FM98IOluCNjYz85FBEKxMULdulYYAsGTJkmxfXx/e3jOIYjuZPGKMOaNUKq2qO8oYBYrF4oHGmF/ZVmHmFUEQ4JrZVPE873Bm/k8RgTIp' \
                 'rrQbY44olUrPxK1Yr3xDAPB9Hxy9q+t1UuXvuHdDRQueXari+/4VInKBTaMi8qcwDJM8EJvmdyhTLBZfb4xpi1hOsdoQke+FYQiiTKqSGA' \
                 'C+7y8Xkf8horhXHmyFH7dV6MSdred54OnZnP7R9PUjrYvHJ5OI/ouIrBVPg9bgE1pr6DZSI6ImAkBk1QP1CVedOPIDrfU/NUvJ4XketI4/' \
                 'sxyQEZF3h2H4Q8vyqRVbsmTJ1N7e3rUJ2E/Picj+aVLNkgCAfd+/TkTiWrEeyOVyJ7a1tW1MbSUHNRRdvfAtx3XURrrL5fLizs5OPIgRF9' \
                 'gXNm7ceFekSo7T/zpjzKGlUunJOJVqlY0LADz894gItGbVPG1q9fMIMx8WBAGMOU0Rz/NAKcMnyebujzFgN4LmbqdJtJPidA/DVRwB+/gz' \
                 'cSqkAoBisfgmY8y9MUys6Hddf3//QWvWrIFXTdPEdd1bI+OMTR/dsPhqrf9oU7iZZaKD4T0xQfCCUupN7e3taxodW6wdwHVdaPqg1LAVGH' \
                 'PeprXGwaxpUiwWjzTGYDu1Ema+OwiCOPOwajdpId/3DxOR/455O3gol8sd2dbWBs5DYrEGQLFYPMEY86M4pl1mPicIAhBBmmbZWrBgwSuz' \
                 '2Sx896wVUSLy3jAMv5941ZpQ0ff9s0TkP2LyJho2YlkBIPpW4YAFEqet3K61frtt4aTlXNcFt+6SGMD8W6VS8To6Op5O2mcz6hUKhV2UUt' \
                 'cSERxjbOVxpdTypBZTdGIFANd1T2Xm62Ms8ovMfGAQBFB6NE0KhcKBSilrrV+0E12utb44zUFBI9rT0zM98l98neM4d/X3968vlUogqFoL' \
                 'bgYbNmwoMfM+1pWIrtRafzLpLmsDAPY8D3d+cONs5VKt9eeboekbGECkY7+dmQ+1HRQR6f7+/jevWbMGZudUxPf9g0Tk34kIn6DBN5AnRe' \
                 'Tacrn81Tj9+b4Putn3YnwKXqhUKss6OjoeSzKhugDwPO9d8HWL0fhKrTX89ZsmEdH0Mma2UvkODISZTw+CAIubhnChUPiUUgrsneHknlwu' \
                 'd0xbWxv4i3UFwJ4+ffodtmxmNCginw/D8J/rNl6lwLAAiL5LoFrvb9v4SBywXNc9j5nx1sURPIjj2tracAVsWHD4zGQy4BDUVYUrpS5ub2' \
                 '//F9tO58+f/5psNvsIEUFtbCPPK6UWtbe3/8Wm8OAywwIgYrfg8LerTcMi8tjkyZOXNno1Ga6vQqGwWCkFF2yEfbEV8AwOHkz7tq1Yq5zn' \
                 'eT8houMt23m+Uqksj7NNe54HnX8cnuLA2SbWjWtYAHieB//8Cy0niS3urc30j/d9f4mIQBEVNzrINfl8/ty0onlEOyMYO7aULzHGHFcqla' \
                 'CptJJisTjfGBOHpdSBkDlxSTU1AQDnTREJYhgs7jXGHBP35Gu1GjhhuS48iq5jZuv7ftT2E8aYFWnpztGm7/u+iLzsRGIzBxH51zAMbV+m' \
                 'bU26rnspM3/Opn0i6oaSLgiCOLei2tdAz/PgzGHNUReRU5tlWYu2/fsSvPn43h+utcYtJjXJ5/P7OI4T14h0sdba+hyAwc6bN2/G5MmTsQ' \
                 'u82nLwsc3bVXeAyFIF1eQ7LTt+MpPJLFy9evULluWtixUKhaOUUtfFOBANbvuSXC53ue0J3HZQOKnvsssuoKtPt6wD4stRcQmeJ510ktPZ' \
                 '2Xk9Xi7LfrqUUoU4h8GqAJg/f/70SZMm/cGS249Dx2fjottiQogMtswYg1uI1SF0cJvM/MMgCGwXzmI42xfxPA/RTE6wrLixUqm8Oc4hcK' \
                 'DdyJX+dst+UOzDWutv2JavCoDIyQF+anVNqyKy0RiTaHLDDBLKp/clpVWLyFrHcQ6N8ybYLthAOfhAOI6DwFA25FM4enw9CZMn8jzCs7Al' \
                 '39yRy+XeabvrVQWA67oXMPMVlosC79wjq3jnWlbfvlgUKOpjRPSJmGbnbQ0BkI7jHNze3q4TDSBGJc/zcKg7e5iDcj/o8mEYQpmWWKJ+cH' \
                 '6oq7gjojXGmP1sae5VG/Q8D6FSbQ0/H9Jaw++/YcE1zxjzFdgRkjaWsrav7jDghQxNHDPD8PXymQCu68aYC2fMmPFQoy9HdCXEQdaGVr61' \
                 'XC7vZRuYagcARASFx+vO/KUCsEXPb5TguWTJkl17enrehWBKNp+dGmPrEpHzwzCEF/GIy7x583JTp051K5XK7EmTJj2yatWqDWkNIjqTwe' \
                 'S92LLNk7XWVur7HQDguu4JzIwDjo3cEJE8bcpWLROxZOFVBCZvNnFDRJ/RWuOzlTrVvIExpVbV8zy4mX3cskHr57IDADzPA9fM5r4K9+1T' \
                 'krhuYxKFQgFm0zNFBFz3RoItwOT6pbRNvJYLPWLFisUiIqHbmtefmzVr1mttQtdW2wGgbXuvxczg03dgAv06iKWniEgcfkGt4QgOq0EQxN' \
                 'KwWcxtVBbxPA/aRyv/SxHZx4Y+Xm0H+DURHWCxAs8opRbaslGw1YvIkUT0/ihwhK0evdZQ+qJvPq5X40I8z8N33fZGcbzW+qf1FqYaAECV' \
                 'srnbrtFaLxiuAzhqbtq0aQ/Hcc5iZli2ptQbkOXfnzPGnBnHuGLZ7qgu5nkeqG9Wdn8R+VQYhvBMHla2A8DChQtfW6lU/mx53/ym1vpDVV' \
                 'qHBm9ppVI5mpnB1Z8fk+1ab8wI5HB2gk9PvXZH/d9jknOu0VpDR2EPgDhqRxEBdek3juPsWqlUZjLzAqRsISJEAW1GcMYeIvpJPp9/Ty2z' \
                 '7qJFi+aWy+VTohg79ebecn+P6GcIGGHz+fyZ1vrYepPcbgeIqMm2Sh3oCrClI/ABgjw3GglsuLE+LyLnzJgx47ZaShXXdU9hZmx5YNEco7' \
                 'WGs8WYksgMjR3QhgyzWmtdV2+wHQBc1wXPLlXGbINPAF6wbcyMSGFVAyQgoKMxBlfXwZ8j+NPvb6sObXCMI1Y9+kSDKmYTxfRprXXdcD1D' \
                 'dwA4fdpcAUdq0p+ZPn36VbXe+kh1/BNmft2Qc4uIyFHNDK0yUgswuB8cqru6usAPwHzryRatdV1z9dAd4N6YNOt6g0jyd1DL7lFKXdbe3g' \
                 '5r2w4SRSZ5l4hcOQxP4Batta25Nsk4d0odz/Pgz7i3Recml8tNrmcV3A4AnuchT96wVzuLjpMWgQq3W0TODMMQARSqCijhjuMgCggshvVk' \
                 'abP9EusNIO2/xwAAun6d1hq3upoyFADw3X9l2oO2aO8vzPz13t7eG9auXfvXWuVd153HzDD2IIOYjbRls9mj0jTM2HTazDJxABB5ED8cBw' \
                 'C2WsA05ogQaE8jpHsul7vKhkruuq6tmnpgfNhVPtcEtlIa80/URhwAZDKZ169evXrYKORDd4CvEtG5iUYWr9JPET4+k8k8Guft9H3/OCL6' \
                 'sYhYXzlFZLMx5u0dHR2x2LLxpjNypWMAoFdrjVD5w8YT2g4A+XzecxwHC4V8PmkK4gT8iYh+bYy5MWlouIisCoIoGMtx5A+ZTObwZpBW4w' \
                 'wijbK2AAAtLgxDaGGHlR1sAb7vfy6lRE4w08IYcQPMmFOmTNmchltWFGAJ7BjbWEDEzHgLvhgEAdLVtKxE3sOPMXO90HZQgoGpVTcCyg4A' \
                 'WLFixeSNGzdCh/yRWnHwsaDYWpl5g4g8x8zPGGMQxPDPyIejlHqyu7u7tG7dOpiMU5dIZQ0vmzhxigCEjwRBAOthLPep1CeQsEELZx2EjP' \
                 'nSrFmzvm/DBcAwhiMZIuL2ocw8W0TgALkLMz9WLpc7Zs6c+ceVK1fiDcdCDizmiC5qQq3l5p6enj2bBcyEz9W6Gkg0SimE25ldpdJ1uVzu' \
                 'PJvD9OC6NixT6wGOZME5c+ZMmTlz5h1w+ozTr4g8hYhlWmvoPFpKisWiZ4yBLWDATwK3HPhNXJXU9tGyAMCTi5xFEWi6rspzyJO+s6en5/' \
                 'hGw9KPNHoQnZWIEJgbybT/Do5FEATITZBYWhoAEQjeYoyBPaCun/52Wx8z3pxTmxm7MPFTqVHR87zTROTt8HqqVCoPJY1z5LruEYVC4V6Y' \
                 '1VseAFiriMmM4JWxXMjAfjbGnBXXpTrtB2vbHszBQRDAYzuRRM6msPZ+Mgou9dCYAABWo1gsnmiM+UECvwIkmnynLbcx0cqPgkpROp9vis' \
                 'jh4G4wcx5ZUsYMALDGnuch8QNIIXHPBA8YY84ulUrwiBrR28xIYMP3/bcQ0bWDnH3fP5CUakwBIDoTHCciddmwVRb+2UhPEDtF3Ug8xIR9' \
                 'wMn2LCJCPKVthNwoishvB9obcwDAxAqFwjKlFPwO6qpChy4sQr5ls9nLWl1tXCgUDnAc5yIRQRi9bR5X1fwmxyQAojPB7sYY0KdAi4o7z8' \
                 'eNMceWSiXoClrK1Sw66EHlDe/qAcEcjqymK4i7MAl3op1TLXI1h09d7DyEcDNXSt0uIl+w0anvnBn+f68IXJXJZBDPGf6DyH4+8GwRzOoD' \
                 'tXIQjmkADCyP53lfQgraGNE3Bz/PjSJySTabvXEUfhbggzGrUqkcGwXN3C7ELDM/hehkYRj+vhZAxwUAopg+SCMLH0Ibr6eh61UWkTVQwC' \
                 'ilvt/MyCO2Ownc+EXkXBEB9x8kUWgHB8vPK5XKWR0dHTDD15RxAYCB2UeBFr5FRAg5lySRI5pCVtMbEdm7p6dn3dq1a5uSAmfoE4uIsHuK' \
                 'yH4iciIzIzNptefXIyLwIUSshLqJOMcVALCoEbUaySLALWyE+PIiEW1k5vtEBPmOYZhKXaLgGUcrpc4QEZ+ZdxuOEcXMt3V1dZ28fv16eF' \
                 'LVlXEHgEHnArivXYjUrEnzHQ9ZXYSNQyxDMKqeVEo93d/f//Qee+yxwcY2jzd869atMxzHmaOUQuZ1hMtZxsz7xVRsIUOLNRjHLQCih6cW' \
                 'LFjwCsdxLkF2k7qvi30BXLvAQtpGdSeiR4kI2/EWEUEsvy3GmK1ENIeZkXd5nlIK7vMguOAHzmMssks0tN9prRHW31qbOd4B8PIjhaHFGH' \
                 'N69G1thnOrPXySlYRDzWm2sYEGupgAwJDFRnqccrl8fpQXESbmRuIWJXuUCWqJyPooXmOsVDgTAKix2IVC4VVKKQSuQqZTZCRNemtI8DgT' \
                 'Vfmy1vpTcTWXEwCwWGvEHahUKh/C9StKEAFr42haO6TAceu5gVWb6miahMWj2LlF8Hno7e3d3XGcgoiAiwgXtULKo0IksGKcTw8MWGEY2o' \
                 'aQ2264EwBo8OlFnwrkSHoDM+8eMajxuZjGzNNEZNv/I00dmNRQJOGHezr+RYT11cz8oOM4D/b393+cmRHvwPYWgLf/gKQhcyYA0CAAqlTn' \
                 'FStWOOvXr8/MmDHDyWazma1bt2aMMZzNZs3kyZMrW7Zsgeu22bx5c2Xp0qX9AyFvCoXCsUophOmvG6R7oF8kmwzDEHaORCnlxw0AojQvez' \
                 'DzVPyMMdv8C0VkBjO/PoozsBsMKND7ZzKZX46k8WfhwoX7VioVpMOJcwVdUy6X97eNCzzuzgCIJaCUQqQyRD3BSd76zSIi0MPOi5vkIeGG' \
                 'AuYOWMoYq7WkkaFtrO4AA2nuB2zj1os6pCC+zwcl/b7adBqB9CtI9GBTflCZR5n54EZp7WMOAAsWLJibyWSQhBnh6tKQq7XWzXKZx5uPyJ' \
                 '81I6LUmAAOkAjT23BW9jEFgCjhIrZSq3i6luj4o9baNluHZZMvFfN9/9MiUi/zaLU2ERk9Sb0d2hozAHBdt8DM8JtrxMRbbbFf0Fqn2mZE' \
                 'VbtoCG/PBjww8txijDk1rfR8YwIAURrXVTFP0DYLjjK/1VrbBM+2bQ+eTLcxc90onlUa7KxUKockdQkbk7cAZNPIZrO3ENFh1k/AsmAUWO' \
                 'KCIAji5imu2kN0PvluXI/mqLENxpjjS6USdrnUpOV3ADg6MvPP4qhOY6xe4qTMQ/soFAquUgpOJ7a5mAY3gdD4CJ8HX4dUpeUBEN2fj0h1' \
                 'VV5qDG/cW0ulElK2JRbkEsrlcrAoXh7Xg3lQp1fncrlPpxFiZ+hEWhoAUXbzhh7QoAUBe6ccMXjuEJHLwzCEMiixwEljypQpcMg8JWEjyI' \
                 'hyVRAE5yesX7daSwPA8zwkT0ASBVt5UkQeZmYQOl9kZtC1NiG+keM4m8rl8jPMXLJh09brsFgsHoIUeJFlr17xWn+/zhhzbjODXrcyABDD' \
                 'CN/U4y1XFyTN+WvWrIH1rGmCg142mwVfH34IsAImlR9prU9OWtm2XssCACza3t7eOy1P/yBkHpGG5qzWwu67776zcrncJ0QEMQwbyYIGJ8' \
                 '6bHMc5eySMUS0LgIjffz8RLauHdhFZJSJvSXsrBQi7u7vnKqXeBtdyIoJVsRHBGQShcz9cL8p3I50MrtuyAIiSKiOJRF21bzMAEKVvgQcu' \
                 'yCAzYxA4aj27rSJyQW9v73dGMnjVeAEAAlYeHYbhy4ERYr5BqlAogMOfZ2ZE6oLZFv+mJY8j/H0YhvikJSJ2JB1IywIgiht8Gx6s5eR/r7' \
                 'Wu+7kYaAsRUzdt2rSfMeYQETmViOB5i/VKe82eZ+ZlQRDY5mu2nK5dsbQnY9drSqU8z4OZFhHObeVBZr5bRJD0Gny9XZkZDF8kvdr2Y+YZ' \
                 'IoKgEq9uknZxYKww7FyZzWa/smrVqqdsJ5B2uVYHANSqUATZpFFLe+0aaQ8xlRG3GDvYTpWWBgBWzvM8pLlDIKRWEBA5kO/gUpu8viMxoZ' \
                 'YHQD6f38dxHKRFSdVmn/Li43qHeEMXaq3viuu9k/JYtmuu5QEQxdC/iZlPauZCNdD2E0T0hUwmc8tIKHbijrPlAYAJFwqFRUopUMGQNXS0' \
                 'SKdS6gfGmG9rrZExZVTKmAAAVjaKF4zQKNb5hJr0RJ5GZDERuT5tzWMzxjtmAIDF8X3/nCjdzW7NWKxh2kScIPj03VapVG5Nk7LV7HmMKQ' \
                 'BEIDhaRG4dgTs8DnbQ4H2tXC7f0GwrY7OAMOYAEIEAfv1IfpWEeFlzrSMewf3GmNtBFu3t7e0cSb19M0AwJgEwsFCR08WZkcEIBhsb1zAw' \
                 'g0AY2UJEMNA8wcxIdwcy5sOt8F2PA5QxDYBoIdTixYv37OvrmxOpd+E/AJ9+5EhGZK9nkfkM/+KnlHpORDZkMpmNfX19G8faAx8KjvEAgD' \
                 'gvxLgrOwGAcffIt5/wBAAmADDOV2CcT39iBxjnAPg/uwCRF5yCt2cAAAAASUVORK5CYII='

        page_mid = gui.Widget(width=320, style={'display': 'block', 'overflow': 'auto', 'text-align': 'center'})
        self.img1 = gui.Image(imgurl, height=100,margin='10px')
        #self.img1 = gui.Image(r'https://github.com/welbur/pysimplegui-prj/blob/master/logo.png?raw=true', height=100,
  #                            margin='10px')
        self.lab1 = gui.Label('识别能力列表', width='100%', height='30px', style={ 'font-size':'25px'})
        self.b1 = gui.Button('表格识别', width=200, height=30, margin='10px')
        self.b2 = gui.Button('文档识别', width=200, height=30)
        self.lab2 = gui.Label('了解更多，请访问：', width=200, height=30, margin='10px', style={'color': '#4B4F70'})
        page_mid.append([self.img1, self.lab1, self.b1, self.b2, self.lab2])

        header_label = gui.Label('AI工具', width='100%', height='30px', style={'background-color': '#ffb509', 'font-size':'25px'})
        #verticalContainer.append([menubar, horizontalContainer])
        verticalContainer.append([header_label, page_mid])
        #this flag will be used to stop the display_counter Timer
        self.stop_flag = False



        # returning the root widget
        return verticalContainer


    def menu_dialog_clicked(self, widget):
        self.dialog = gui.GenericDialog(title='Dialog Box', message='Click Ok to transfer content to main page', width='500px')
        self.dtextinput = gui.TextInput(width=200, height=30)
        self.dtextinput.set_value('Initial Text')
        self.dialog.add_field_with_label('dtextinput', 'Text Input', self.dtextinput)

        self.dcheck = gui.CheckBox(False, width=200, height=30)
        self.dialog.add_field_with_label('dcheck', 'Label Checkbox', self.dcheck)
        values = ('Danny Young', 'Christine Holand', 'Lars Gordon', 'Roberto Robitaille')
        self.dlistView = gui.ListView.new_from_list(values, width=200, height=120)
        self.dialog.add_field_with_label('dlistView', 'Listview', self.dlistView)

        self.ddropdown = gui.DropDown.new_from_list(('DropDownItem 0', 'DropDownItem 1'),
                                                    width=200, height=20)
        self.dialog.add_field_with_label('ddropdown', 'Dropdown', self.ddropdown)

        self.dspinbox = gui.SpinBox(min=0, max=5000, width=200, height=20)
        self.dspinbox.set_value(50)
        self.dialog.add_field_with_label('dspinbox', 'Spinbox', self.dspinbox)

        self.dslider = gui.Slider(10, 0, 100, 5, width=200, height=20)
        self.dspinbox.set_value(50)
        self.dialog.add_field_with_label('dslider', 'Slider', self.dslider)

        self.dcolor = gui.ColorPicker(width=200, height=20)
        self.dcolor.set_value('#ffff00')
        self.dialog.add_field_with_label('dcolor', 'Colour Picker', self.dcolor)

        self.ddate = gui.Date(width=200, height=20)
        self.ddate.set_value('2000-01-01')
        self.dialog.add_field_with_label('ddate', 'Date', self.ddate)

        self.dialog.confirm_dialog.connect(self.dialog_confirm)
        self.dialog.show(self)

    def dialog_confirm(self, widget):
        result = self.dialog.get_field('dtextinput').get_value()
        self.txt.set_value(result)

        result = self.dialog.get_field('dcheck').get_value()
        self.check.set_value(result)

        result = self.dialog.get_field('ddropdown').get_value()
        self.dropDown.select_by_value(result)

        result = self.dialog.get_field('dspinbox').get_value()
        self.spin.set_value(result)

        result = self.dialog.get_field('dslider').get_value()
        self.slider.set_value(result)

        result = self.dialog.get_field('dcolor').get_value()
        self.colorPicker.set_value(result)

        result = self.dialog.get_field('ddate').get_value()
        self.date.set_value(result)

        result = self.dialog.get_field('dlistView').get_value()
        self.listView.select_by_value(result)

    # listener function
    def on_img_clicked(self, widget):
        self.lbl.set_text('Image clicked!')

    def on_table_row_click(self, table, row, item):
        self.lbl.set_text('Table Item clicked: ' + item.get_text())

    def on_button_pressed(self, widget):
        self.lbl.set_text('Button pressed! ')
        self.bt.set_text('Hi!')

    def on_text_area_change(self, widget, newValue):
        self.lbl.set_text('Text Area value changed!')

    def on_spin_change(self, widget, newValue):
        self.lbl.set_text('SpinBox changed, new value: ' + str(newValue))

    def on_check_change(self, widget, newValue):
        self.lbl.set_text('CheckBox changed, new value: ' + str(newValue))

    def open_input_dialog(self, widget):
        self.inputDialog = gui.InputDialog('Input Dialog', 'Your name?',
                                           initial_value='type here',
                                           width=500, height=160)
        self.inputDialog.confirm_value.connect(
            self.on_input_dialog_confirm)

        # here is returned the Input Dialog widget, and it will be shown
        self.inputDialog.show(self)

    def on_input_dialog_confirm(self, widget, value):
        self.lbl.set_text('Hello ' + value)

    def open_fileselection_dialog(self, widget):
        self.fileselectionDialog = gui.FileSelectionDialog('File Selection Dialog', 'Select files and folders', False,
                                                           '.')
        self.fileselectionDialog.confirm_value.connect(
            self.on_fileselection_dialog_confirm)

        # here is returned the Input Dialog widget, and it will be shown
        self.fileselectionDialog.show(self)

    def on_fileselection_dialog_confirm(self, widget, filelist):
        # a list() of filenames and folders is returned
        self.lbl.set_text('Selected files: %s' % ','.join(filelist))
        if len(filelist):
            f = filelist[0]
            # replace the last download link
            fdownloader = gui.FileDownloader("download selected", f, width=200, height=30)
            self.subContainerRight.append(fdownloader, key='file_downloader')

    def list_view_on_selected(self, widget, selected_item_key):
        """ The selection event of the listView, returns a key of the clicked event.
            You can retrieve the item rapidly
        """
        self.lbl.set_text('List selection: ' + self.listView.children[selected_item_key].get_text())

    def drop_down_changed(self, widget, value):
        self.lbl.set_text('New Combo value: ' + value)

    def slider_changed(self, widget, value):
        self.lbl.set_text('New slider value: ' + str(value))

    def color_picker_changed(self, widget, value):
        self.lbl.set_text('New color value: ' + value)

    def date_changed(self, widget, value):
        self.lbl.set_text('New date value: ' + value)

    def menu_save_clicked(self, widget):
        self.lbl.set_text('Menu clicked: Save')

    def menu_saveas_clicked(self, widget):
        self.lbl.set_text('Menu clicked: Save As')

    def menu_open_clicked(self, widget):
        self.lbl.set_text('Menu clicked: Open')

    def menu_view_clicked(self, widget):
        self.lbl.set_text('Menu clicked: View')

    def fileupload_on_success(self, widget, filename):
        self.lbl.set_text('File upload success: ' + filename)

    def fileupload_on_failed(self, widget, filename):
        self.lbl.set_text('File upload failed: ' + filename)

    def on_close(self):
        """ Overloading App.on_close event to stop the Timer.
        """
        self.stop_flag = True
        super(MyApp, self).on_close()


if __name__ == "__main__":
    # starts the webserver
    # optional parameters
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    import ssl
    start(MyApp, debug=True, address='0.0.0.0', port=8081, start_browser=True, multiple_instance=True)
