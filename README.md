## Archdaily

[ArchDaily](https://www.archdaily.com/) is a weblog covering architectural news, projects,products, events, interviews and competitions, opinion pieces, among others, catering to architects, designers and other interested parties.

![](https://github.com/BahramJannesar/ArchdailyProjectDownloader/blob/master/image/logo.jpg)

### Idea 
I have too much architect friends, all of them whenever to want to find an idea about their project, first of all, check the Arcdaily website and tell me how can I download information and pictures of these projects, because of this I try to write this project for them but, I can't turn this project to usable product for architects. everyone do this job, It has been a great help to the community of architects.

### Dependencies

    pip install selenium
    pip install bs4
    pip install requests
   
   and must download the [chromedriver](https://chromedriver.chromium.org/) compatible with your chrome or [firefox driver](https://developer.mozilla.org/en-US/docs/Web/WebDriver) if you use firefox.
   
### Project detail
every project in Arcdaily has the project id and you can find this from here 

![](https://github.com/BahramJannesar/ArchdailyProjectDownloader/blob/master/image/id.png)

project deatails are download in .JSON file like this 

      {
    "Project ID": "939672",
    "Project Titel": "Emergency Public Hospital in São Bernardo do Campo",
    "Project Type": "HOSPITAL",
    "City": "SÃO BERNARDO DO CAMPO",
    "Country": "BRAZIL",
    "Architects": "ARQLAB, SPBR Arquitetos, [sic] arquitetura",
    "Area": "234998 ft²",
    "Year": "2016",
    "Photographs": "Nelson Kon",
    "Project URL": "https://www.archdaily.com/939672",
    "Text Content": [
        "Text description provided by the architects. The industrial city of São Bernardo do Campo, in the metropolitan area of Sao Paulo, played a remarkable role in the recent democracy in Brazil. It was there where the former president Lula arose as a syndicalist to found the workers party, PT, in 1980. Under the second consecutive government of the mayor Luiz Marinho, the Board of Health nowadays is led by Odete Carmem Gialdi — who succeeded Arthur Chioro, currently incumbent of the Ministry of Health in Brasilia — whose headship focuses on strategies to assure assistance of quality for all.",
       
        "Besides, Alfredo Buso, architect ahead of the Department of Urban Planning, has imprinted important improvement in the urban scale highlighting mobility and flood control. In addition he has been dedicate to emphasize the role of architecture in the process of improving urban quality by both preserving heritage as a school designed by Paulo Mendes da Rocha in the sixties or creating possibilities for new projects such as the Work and Workers Museum by Marcelo Ferraz and Francisco Fanucci.",
       
        "The Emergency Public Hospital, directed by Renata Martello, is part of the municipal hospital complex and health facilities buildings managed by the ABC Foundation. This hospital works as an entrance to the complex, called as door hospital, it is the first destination for ambulances assisting accidents and emergency calls. Its activities combines pediatric and adult hospitals which share some support but work as two independent buildings. Considered as an emergency hospital it is guided by new concepts about management of diseases classification through a triage process and patient flows using the fast track principle.",
      
        "The building occupies 17.500 m², a whole very long and narrow block. Joaquim Nabuco Street was taken as its public main façade, while Cacilda da Cruz Ferreira works as an internal street for ambulance, staff and service access. The building was divided in two long volumes overlapped:",
       
        "At the bottom, as a three storey high podium measuring 185m and about 35m wide, the lower part of the building has receptions and first care at the ground level, surgery at the first level and, finally, mechanical and support at the second level [usually displayed at the basement, these functions were displaced up due to the very shallow water table and safety level concerning to the history of flood in that neighborhood].",
      
        "On the top of this podium, as a pilotis or an open space, the administration office and educational program were displayed featured as a resting outside area.",
       
        "The upper volume, as a three storeys bar measuring 115m long and 15m wide, hosts 159 hospital beds for both pediatric and adult hospitalization.",
       
        "The extensiveness of this facility building, added to a not clearly defined public space in its surrounding, have offered us the possibility to propose a new design for both Cacilda da Cruz Ferreira and Joaquim Nabuco Street. In the public side at Joaquim Nabuco the building was gifted with a square shaded by trees carefully designed as a landscape, which offer a nice transition between outside and inside."
    ]
     }
