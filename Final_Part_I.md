# Final: Explorations of Environmental Justice in Pittsburgh
To return to the front page, click [here](https://jameson-c.github.io/viz-portfolio).
## Background

### On Redlining in Pittsburgh
Racist policies regulating space in the United States resonate to this day. Across America, cities produced maps which measured communities based on their security grade. These security grades were key to preventing Black and other 'undesirable' types of families from taking advantage of new federal programs which insured mortgages. A red line would be drawn on the security grade map bankers used to determine creditworthiness, essentially telling them "do not lend to these people." This practice became known as redlining. The resulting map as of 1937:

![Screenshot](Redlining.png)

On the forms used to create Pittsburgh's original security grade map, there were fields to denote the percentages of Black and Foreign-born families as well as judgements about whether the community was being 'infiltrated' by 'undesirables.' Very few communities where Black families were mentioned received a B or better, and none received an A. Black families were viewed as especially detrimental to a commmunities' security. The impacts of that racist notion persist. Today, Pittsburgh has a serious homeownership gap between White and Black families due to this and other ensuing policies which created racialized barriers to homeownership. But this injustice and its intersections with other historic zoning policies led to more than just the homeownership gap.

### On Redlining, Industrial Zoning, and Environmental Injustice
Before redlining, many cities produced zoning maps that were used to enforce racial divides. After explicit segregational zoning was banned (though it continued in practice) by the Supreme Court in 1917, a new tactic emerged.[^1] By creating zones where only single-family homes could be built and then blocking Black families from homeownership, cities regulated their landscapes to enforce racist hierarchies. Zoning became a popular way of regulating space during this time. Henry John Heinz and Andrew Mellon, two titans of Pittsburgh industrial history, advocated heavily for a comprehensive zoning plan as they led the Citizens Committee on City Planning in 1918. Mellon and Heinz were highly concerned about the "invasion of single-family residence districts by large apartment houses," apartment houses being associated with the 'undesirables' who occupied them.[^2] The debates leading up to Pittsburgh's first zoning plan centered around preserving neighborhood values, and at the time this meant keeping Black families out of those neighborhoods.

The final ordinance passed in 1923 defined five districts: Heavy Industrial, Light Industrial, Commercial, "A" Residence, and "B" Residence. The maps largely maintained the existing industrial and residential patterns seen in Pittsburgh at the time.[^3] Industry was largely zoned to areas near the river and transit corridors leading into the city. These zones, though they reflected the necessary logistics of industrial manufacturing, also reflected racist practices and history. And further, they set the legacies of that history in stone. One of the purposes of industrial zoning was to keep factories away from White neighborhoods. Zoning also insured White property values by ensuring that few industrial or environmentally unsafe businesses could enter their neighborhoods. Polluters had no choice but to continue to build and operate in disproportionately Black neighorhoods.[^4] All the while, Black families were systematically barred from neighborhoods located further from the industrial core of the city.

These zoning and redlining decisions led to an environment where Black Pittsburghers were (and continue to be) systematically exposed to pollutants. For example, in the field notes used to inform redlining maps, many of the areas with Black residents were designated as having smoke from the steel mills. None of the 'A' security grade zones, which were entirely White, displayed any mention of smoke. To this day, Black Pittsburghers experience worse health outcomes that are associated with pollution.[^5] This is the subject I would like to explore in my final project. I hope to use data viz to explore some of these injustices and call my readers to action. 
## Outline
For this project, I am interested in conveying the history I just described, then shifting toward modern legacies of that history, and finally asking my readers to act. My hope is to inspire readers to contribute to environemntal justice organizations in the area.
Generally, this will 

### The Data

### Initial Wireframes and Plots
#### Examining historic redlining data and locations of modern factories
For this exercise, I opted to try and evaluate the relationship between redlining and environmental hazards in those communities. First, I obtained data tracking large emitters of greenhouse gases from the EPA's [FLIGHT database](https://ghgdata.epa.gov/ghgp/main.do#/facility/?q=Pittsburgh&st=PA&bs=&et=&fid=&sf=11001100&lowE=-20000&highE=23000000&g1=1&g2=1&g3=1&g4=1&g5=1&g6=0&g7=1&g8=1&g9=1&g10=1&g11=1&g12=1&s1=1&s2=1&s3=1&s4=1&s5=1&s6=1&s7=1&s8=1&s9=1&s10=1&s201=1&s202=1&s203=1&s204=1&s301=1&s302=1&s303=1&s304=1&s305=1&s306=1&s307=1&s401=1&s402=1&s403=1&s404=1&s405=1&s601=1&s602=1&s701=1&s702=1&s703=1&s704=1&s705=1&s706=1&s707=1&s708=1&s709=1&s710=1&s711=1&s801=1&s802=1&s803=1&s804=1&s805=1&s806=1&s807=1&s808=1&s809=1&s810=1&s901=1&s902=1&s903=1&s904=1&s905=1&s906=1&s907=1&s908=1&s909=1&s910=1&s911=1&si=&ss=&so=0&ds=E&yr=2020&tr=current&cyr=2020&ol=0&sl=0&rs=ALL). Then, I overlaid a map of the communities that were redlined in the 1930's, obtained by the [Mapping Inequality Project](https://dsl.richmond.edu/panorama/redlining/#loc=11/40.442/-80.172&city=pittsburgh-pa&text=downloads).

From here, I produced the following map:
<div class='tableauPlaceholder' id='viz1663907129166' style='position: relative'><noscript><a href='#'><img alt='Modern large emitters in Pittsburgh are generally located in areas which were redlined in the 30&#39;s ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pi&#47;PittsburghRedlining&#47;Sheet1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='PittsburghRedlining&#47;Sheet1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pi&#47;PittsburghRedlining&#47;Sheet1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>
<script type='text/javascript'>
  var divElement = document.getElementById('viz1663907129166');
  var vizElement = divElement.getElementsByTagName('object')[0]
  vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';
  
  var scriptElement = document.createElement('script');
  scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
  
  vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>

### Method and Medium

[^1]: Rothstein, Richard. 2018. The Color of Law: A Forgotten History of how Our Government Segregated America. New York, NY: Liveright Publishing Corporation. 55-56.
[^2]: Lloyd, Anne. 1974. Pittsburgh's 1923 Zoning Ordinance. Pittsburgh, PA: Carnegie Mellon University. 296.
[^3]: Ibid., 303.
[^4]: Rothstein, Richard. 2018. The Color of Law: A Forgotten History of how Our Government Segregated America. New York, NY: Liveright Publishing Corporation. Chapter 3.
[^5] Marusic, Kristina. 2020. Environmental injustice in Pittsburgh: Poor, minority neighborhoods see higher rates of deaths from air pollution. Environmental Health News. https://www.ehn.org/environmental-injustice-pittsburgh-air-pollution-2646169635/particle-1


