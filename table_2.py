import pandas as pd
import html5lib
url = 'https://mcs.ciena.com/InetReports/AssemblyHistory/ResultsByAO.asp?SN=NNTMRT112ND8&PN=NTK540BC-820&R=008'
df = pd.read_html(url)
df[2]
