# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 10:06:51 2020

@author: xXJaneXx
"""


from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app_toy import HDapp,server

layout = [dcc.Markdown("""
### References
1. 	Hervatis V. Project management and tools for HI [Internet]. Stockholm; 2020 Sep [cited 2020 Sep 22]. Available from: https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1365-2934.2006.00624.x
2. 	Hollmén J. PROHI 2020: Assignment for Data Mining [Internet]. Stockholm; 2020 Sep [cited 2020 Sep 22]. Available from: http://archive.ics.uci.edu/ml/datasets/Heart+Disease
3. 	WHO. Cardiovascular diseases (CVDs) [Internet]. 2017 [cited 2020 Sep 18]. Available from: https://www.who.int/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds)
4. 	Chaurasia V, Pal S. Data Mining Approach to Detect Heart Diseases. Int J Adv Comput Sci Inf Technol. 2013 Nov;2(4):56–66. 
5. 	Kavihta Rani B, Srinivas K, Govrhan A. Applications of Data Mining Techniques in Healthcare and Prediction of Heart Attacks. Int J Comput Sci Eng. 2010;02(02):250–5. 
6. 	Aziz A, Rehman AU. Detection of Cardiac Disease using Data Mining Classification Techniques. Int J Adv Comput Sci Appl. 2017;8(7):256–9. 
7. 	Fatima M, Basharat I, Khan SA, Anjum AR. Biomedical (cardiac) data mining: Extraction of significant patterns for predicting heart condition. In: 2014 IEEE Conference on Computational Intelligence in Bioinformatics and Computational Biology, CIBCB 2014. IEEE Computer Society; 2014. 
8. 	Bilal MM, Hussain M, Basharat I, Fatima M. Cardiac data mining (CDM); organization and predictive analytics on biomedical (cardiac) data. In: AIP Conference Proceedings [Internet]. 2013 [cited 2020 Sep 18]. p. 260–9. Available from: http://aip.scitation.org/doi/abs/10.1063/1.4825018
9.  How to refer - Rapid access chest pain clinic [Internet]. [cited 2020 Oct 27]. Available from: https://www.uclh.nhs.uk/OURSERVICES/SERVICEA-Z/CARDIACS/RACPC/Pages/refer.aspx
 
""")]