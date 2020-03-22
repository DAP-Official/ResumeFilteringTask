# install python-docx and not docx 

from docx import Document

def convertDocxToText(path):
	document = Document(path)
	return '\n'.join([para.text for para in document.paragraphs])

'''
Name				: Vasanthi Kasinathan
National			: Singapore P.R.
Current Drawn Salary	: $9k per/mth
Notice Period			: 2 Months


EDUCATION DETAILS

Singapore Accountants Academy 
	ACCA (1997)
	FCCA (2002)

Institute of Business Studies (1987)
	LCCI Diploma in Cost Accounting

Methodist Girls Secondary School, Malaysia (1985)
	GCE ‘O’ Levels

LANGUAGE SKILLS

Fluent in English, Malay

TECHNICAL SKILLS

Proficient in Microsoft Office Suite
JDE One World, FinanceOne, Quickbooks, IBM S36, Accpac (Accounting Softwares)
Easypay, Readypay (Payroll Software)
	

PROFESSIONAL EXPERIENCE

Pacific Star Financial Pte Ltd Oct 2010 - Present
Fund Controller

Portfolio 1 :-
Real estate close ended fund with assets located in Thailand, Korea, Singapore and Malaysia with total investment size of ~EUR1.25bn.  The fund invested in prime commercial and residential real estate in gateway Asian cities in Singapore, Malaysia, Thailand, Hong Kong, China, Japan and Korea.

Portfolio 2 :-
Real estate close ended fund with assets located in Thailand and Malaysia. The fund invested in residential real estate in Malaysia. 

Key Responsibilities：

Monthly/Quarterly
Overseeing all aspects of financial control in the fund management business
Review monthly reports prepared by external property managers
Review SPVs onshore/offshore and holding company books at entity and consolidation level and 
		ensure reconciliation on monthly basis (bank, inter-company, accruals etc) 
Maintain SPVs bank accounts and serve as director of SPVs
Manage bank mandates, annual statutory audit, annual budgets, forecasts, annual tax returns and 
		quarterly GST returns
Review quarterly reports to investors, budget variances and ad-hoc analysis
Involved in Business Planning, P&L, Balance sheet & liquidity planning
Overseeing internal financial controls
Liaise with banks/trustees on loan compliance ensure no breaching of loan covenants etc
Undertake Cash management

Annually
Co-ordinate with Asset Management team on annual budgets
Liaise with auditors on annual audit exercise and tax agents on annual tax returns

Ad-hoc
Assist Fund Management team on external refinancing of SGD650 million loan
Co-ordinate with Fund Management team on due diligence of divestment, cash repatriation during the 
		life of investment and divestment: -
Korea - KRW 235bn
Singapore - SGD 970mn
Malaysia – MYR 160mn
Thailand – THB 2.3 bn
Calculate capital call and distribution to investors
Calculate performance of fund IRR

Frasers Centrepoint Asset Management (Commercial) Ltd (REIT Manager) Apr 2005 – Mar 2010
formerly known as Allco (Singapore) Limited (Acquired by Frasers Group in August 2008)
Allco (Singapore) Limited 
(Allco Finance Group JV with International Mezzanine Fund Management Ltd)
Senior Finance Manager

Key Responsibilities:

REIT
Consolidation and management reporting of the Group’s and REIT’s statutory accounts 
Responsible for SGX reporting requirements, announcement and review of subsidiaries’ financial 
	reports 
Direct the budget process and manage internal financial controls as well as statutory compliance of 
	local group of companies 
Implementation of accounting procedures and financial management functions including financial 
	accounting, cash management, budgetary matters, external audit, management reporting. 
Advise operations on treasury matters such as loan roll-over notices, bank covenants, prepare cashflow 
	projections, etc.

CORPORATE
Manage the accounting and operations of Singapore entity
Reporting to Head office based in Australia on monthly basis (Allco Finance Group)
Preparation of annual reports, tax returns and co-ordinate with the Company Secretary on annual return 
	and other corporate secretarial matters
Supervise GST reporting
Supervise payroll, CPF reporting and IR8A
Liaise with bankers, auditors, tax agents and external company secretary and reporting on overall 
	internal control and giving recommendations on improvement 
Responsible for due diligence on sale of Allco (Singapore) Ltd to Frasers & Neave Group
Integration of accounting systems (JDE One World & FinanceOne)
Other projects as assigned

International Mezzanine Fund Management Ltd (Fund Management)
Finance Manager
Period: 2004 – 2005 

Internet Security Systems Pte Ltd (Southeast Asia & India) (Internet Security Provider)
Accountant cum HR & Admin Manager
Period: 2000 – 2004 
 
Tang Cheng Lin & Co (Public Accountant)
Payroll & Accounts Executive
Period: 1998 - 1999
 
BSN Commercial Bank, Melaka, Malaysia (Bank)
Bank Officer
Period: 1997 – 1998 

Matsushita Denshi (S) Pte Ltd (Semi-conductor)
Accounts Assistant	
Period: 1995 - 1997 

Neptune Orient Lines Ltd (NOL) (Shipping)
Assistant Executive 
Period: 1990 - 1995
'''

