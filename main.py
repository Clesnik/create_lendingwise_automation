from fastapi import FastAPI
from pydantic import BaseModel
import asyncio
from typing import Optional
from playwright.async_api import async_playwright

app = FastAPI()

class ActionRequest(BaseModel):
    username: str
    password: str
    branch_id: str
    secondary_agent: str
    loan_program: str
    internal_program: str
    prop_process: str
    primary_status: str
    lead_source: str
    referring_party: str
    pg_one_fname: str
    pg_one_mname: str
    pg_one_lname: str
    pg_one_email: str
    pg_one_cell: str
    pg_one_work: str
    pg_one_street: str
    pg_one_unit: str
    pg_one_city: str
    pg_one_state: str
    pg_one_zip: str
    pg_one_county: str
    pg_one_country: str
    mailing_street: str
    mailing_unit: str
    mailing_city: str
    mailing_state: str
    mailing_zip: str
    mailing_country: str
    pg_one_dob: str
    pg_one_ssn: str
    pg_one_marital_status: str
    pg_one_citizenship: str
    pg_one_mid_fico: str
    pg_one_fico_range: str
    borrower_type: str
    entity_name: str
    trade_name: str
    entity_type: str
    date_of_formation: str
    state_of_formation: str
    ein_number: str
    business_phone: str
    entity_address: str
    entity_city: str
    entity_state: str
    entity_zip: str
    member_name_zero: str
    member_title_zero: str
    member_ownership_zero: str
    member_address_zero: str
    member_cell_zero: str
    member_ssn_zero: str
    member_dob_zero: str
    member_email_zero: str
    member_fico_score_zero: str
    member_guarantor_zero: str
    member_citizenship_zero: str
    member_name_one: str
    member_title_one: str
    member_ownership_one: str
    member_address_one: str
    member_cell_one: str
    member_ssn_one: str
    member_dob_one: str
    member_email_one: str
    member_fico_score_one: str
    member_guarantor_one: Optional[str] = None
    member_citizenship_one: Optional[str] = None
    member_name_two: str
    member_title_two: str
    member_ownership_two: str
    member_address_two: str
    member_cell_two: str
    member_ssn_two: str
    member_dob_two: str
    member_email_two: str
    member_fico_score_two: str
    member_guarantor_two: Optional[str] = None
    member_citizenship_two: Optional[str] = None
    member_name_three: str
    member_title_three: str
    member_ownership_three: str
    member_address_three: str
    member_cell_three: str
    member_ssn_three: str
    member_dob_three: str
    member_email_three: str
    member_fico_score_three: str
    member_guarantor_three: Optional[str] = None
    member_citizenship_three: Optional[str] = None
    member_name_four: str
    member_title_four: str
    member_ownership_four: str
    member_address_four: str
    member_cell_four: str
    member_ssn_four: str
    member_dob_four: str
    member_email_four: str
    member_fico_score_four: str
    member_guarantor_four: Optional[str] = None
    member_citizenship_four: Optional[str] = None
    member_name_five: str
    member_title_five: str
    member_ownership_five: str
    member_address_five: str
    member_cell_five: str
    member_ssn_five: str
    member_dob_five: str
    member_email_five: str
    member_fico_score_five: str
    member_guarantor_five: Optional[str] = None
    member_citizenship_five: Optional[str] = None
    additional_guarantors: str
    pg_three_fname: str
    pg_three_mname: str
    pg_three_lname: str
    pg_three_cell: str
    pg_three_ssn: str
    pg_three_dob: str
    pg_three_marital_status: str
    pg_three_street: str
    pg_three_city: str
    pg_three_state: str
    pg_three_zip: str
    pg_three_email: str
    pg_three_citizenship: Optional[str] = None
    pg_four_fname: str
    pg_four_mname: str
    pg_four_lname: str
    pg_four_cell: str
    pg_four_ssn: str
    pg_four_dob: str
    pg_four_marital_status: str
    pg_four_street: str
    pg_four_city: str
    pg_four_state: str
    pg_four_zip: str
    pg_four_email: str
    pg_four_citizenship: Optional[str] = None
    is_bankrupt: Optional[str] = None
    is_outstanding_judgement: Optional[str] = None
    is_active_lawsuit: Optional[str] = None
    is_forclosure: Optional[str] = None
    is_delinquent: Optional[str] = None
    is_fraud: Optional[str] = None
    borrower_designated_beneficiary: Optional[str] = None
    flip_experience: Optional[str] = None
    flips_completed: Optional[str] = None
    ground_up_experience: Optional[str] = None
    ground_ups_completed: Optional[str] = None
    is_borrower_gc: Optional[str] = None
    rental_experience: Optional[str] = None
    rentals_owned: Optional[str] = None
    have_professional_licences: Optional[str] = None
    professional_licences: Optional[str] = None
    liquid_assets: str
    desired_closing_date: str
    desired_loan_amount: str
    type_of_loan_requesting: str
    trial_payment_date: str
    maturity_date: str
    loan_term: str
    interest_rate: str
    lien_terms: str
    amortization_type: Optional[str] = None
    is_taxes_ins_escrowed: Optional[str] = None
    taxes: str
    annual_premium: str
    cost_basis: str
    home_value: str
    max_amount_to_put_down: str
    subject_property_address: str
    subject_property_unit: str
    subject_property_city: str
    subject_property_state: str
    subject_property_zip: str
    subject_property_county: str
    subject_property_apn: str
    subject_property_block: str
    subject_property_lot: str
    subject_property_type: str
    subject_property_sqft: str
    subject_property_acres: str
    subject_property_year_built: str
    bedrooms: str
    bathrooms: str
    half_bathrooms: str
    number_of_buildings: str
    number_of_units_occupied: str
    number_of_parcels: str
    estimated_property_value: str
    present_occupancy: str

async def run_playwright_actions(request: ActionRequest):
    results = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1280, 'height': 720})
        page = await context.new_page()
        await page.goto("https://app.brrrr.com/backoffice/LMRequest.php?eOpt=0&cliType=PC&tabOpt=QAPP&moduleCode=HMLO&supp=help")
        results.append("Navigated to BRRRR backoffice login")
        await page.wait_for_selector('input#userName', timeout=10000)
        email_field = page.locator('input#userName')
        await email_field.click()
        results.append("Clicked username field")
        await email_field.fill(request.username)
        results.append(f"Filled with {request.username}")
        pwd_input = page.locator('input#pwd')
        await pwd_input.wait_for(timeout=10000)
        await pwd_input.click()
        results.append("Clicked password field")
        await pwd_input.fill(request.password)
        results.append(f"Filled with {request.password}")
        await page.click("button#submitbutton")
        results.append("Clicked login button")
        # Wait for URL after login
        await page.wait_for_url("https://app.brrrr.com/backoffice/LMRequest*", timeout=20000)
        results.append("Waited for post-login URL")
        # Now perform all the additional actions, appending results for each
        await page.select_option('select#branchId', value=request.branch_id)
        results.append(f"Selected branchId with {request.branch_id}")
        await page.select_option('select#secondaryAgentId', label=request.secondary_agent)
        results.append(f"Selected secondaryAgentId with {request.secondary_agent}")
        await page.click('div#LMRClientType_chosen')
        results.append("Clicked LMRClientType_chosen")
        await page.click(f'ul.chosen-results li.active-result:has-text(\"{request.loan_program}\")')
        results.append(f"Selected loan program {request.loan_program}")
        await page.click('div#LMRInternalLoanProgram_chosen')
        results.append("Clicked LMRInternalLoanProgram_chosen")
        await page.click(f'ul.chosen-results li.active-result:has-text(\"{request.internal_program}\")')
        results.append(f"Selected internal program {request.internal_program}")
        await page.select_option('#propDetailsProcess', value=request.prop_process)
        results.append(f"Selected propDetailsProcess with {request.prop_process}")
        await page.select_option('#primaryStatus', value=request.primary_status)
        results.append(f"Selected primaryStatus with {request.primary_status}")
        await page.fill('#leadSource', value=request.lead_source)
        results.append(f"Filled leadSource with {request.lead_source}")
        await page.fill('#referringParty', value=request.referring_party)
        results.append(f"Filled referringParty with {request.referring_party}")
        await page.fill('#borrowerFName', value=request.pg_one_fname)
        results.append(f"Filled borrowerFName with {request.pg_one_fname}")
        await page.fill('#borrowerMName', value=request.pg_one_mname)
        results.append(f"Filled borrowerMName with {request.pg_one_mname}")
        await page.fill('#borrowerLName', value=request.pg_one_lname)
        results.append(f"Filled borrowerLName with {request.pg_one_lname}")
        await page.fill('#borrowerEmail', value=request.pg_one_email)
        results.append(f"Filled borrowerEmail with {request.pg_one_email}")
        await page.fill('#cellNo', value=request.pg_one_cell)
        results.append(f"Filled cellNo with {request.pg_one_cell}")
        await page.fill('#workNumber', value=request.pg_one_work)
        results.append(f"Filled workNumber with {request.pg_one_work}")
        await page.fill('#presentAddress', value=request.pg_one_street)
        results.append(f"Filled presentAddress with {request.pg_one_street}")
        await page.fill('#presentUnit', value=request.pg_one_unit)
        results.append(f"Filled presentUnit with {request.pg_one_unit}")
        await page.fill('#presentCity', value=request.pg_one_city)
        results.append(f"Filled presentCity with {request.pg_one_city}")
        await page.select_option('#presentState', value=request.pg_one_state)
        results.append(f"Selected presentState with {request.pg_one_state}")
        await page.fill('#presentZip', value=request.pg_one_zip)
        results.append(f"Filled presentZip with {request.pg_one_zip}")
        await page.select_option('#presentCounty', value=request.pg_one_county)
        results.append(f"Selected presentCounty with {request.pg_one_county}")
        await page.select_option('#presentCountry', value=request.pg_one_country)
        results.append(f"Selected presentCountry with {request.pg_one_country}")
        await page.fill('#mailingAddress', value=request.mailing_street)
        results.append(f"Filled mailingAddress with {request.mailing_street}")
        await page.fill('#mailingUnit', value=request.mailing_unit)
        results.append(f"Filled mailingUnit with {request.mailing_unit}")
        await page.fill('#mailingCity', value=request.mailing_city)
        results.append(f"Filled mailingCity with {request.mailing_city}")
        await page.select_option('#mailingState', value=request.mailing_state)
        results.append(f"Selected mailingState with {request.mailing_state}")
        await page.fill('#mailingZip', value=request.mailing_zip)
        results.append(f"Filled mailingZip with {request.mailing_zip}")
        await page.select_option('#mailingCountry', value=request.mailing_country)
        results.append(f"Selected mailingCountry with {request.mailing_country}")
        await page.fill('#borrowerDOB', value=request.pg_one_dob)
        results.append(f"Filled borrowerDOB with {request.pg_one_dob}")
        await page.click('body', position={'x': 10, 'y': 10})
        results.append("Clicked body after DOB")
        await page.fill('#ssn', value=request.pg_one_ssn)
        results.append(f"Filled ssn with {request.pg_one_ssn}")
        await page.wait_for_selector(f'label[for="{request.pg_one_marital_status}"]', timeout=10000)
        await page.click(f'label[for="{request.pg_one_marital_status}"]')
        results.append(f"Clicked marital status {request.pg_one_marital_status}")
        await page.wait_for_selector(f'label[for="{request.pg_one_citizenship}"]', timeout=10000)
        await page.click(f'label[for="{request.pg_one_citizenship}"]')
        results.append(f"Clicked citizenship {request.pg_one_citizenship}")
        await page.fill('#midFicoScore', value=request.pg_one_mid_fico)
        results.append(f"Filled midFicoScore with {request.pg_one_mid_fico}")
        await page.select_option('#borCreditScoreRange', value=request.pg_one_fico_range)
        results.append(f"Selected borCreditScoreRange with {request.pg_one_fico_range}")
        await page.select_option('#borrowerType', value=request.borrower_type)
        results.append(f"Selected borrowerType with {request.borrower_type}")
        await page.fill('#entityName', value=request.entity_name)
        results.append(f"Filled entityName with {request.entity_name}")
        await page.fill('#tradeName', value=request.trade_name)
        results.append(f"Filled tradeName with {request.trade_name}")
        await page.select_option('#entityType', value=request.entity_type)
        results.append(f"Selected entityType with {request.entity_type}")
        await page.fill('#dateOfFormation', value=request.date_of_formation)
        results.append(f"Filled dateOfFormation with {request.date_of_formation}")
        await page.click('body', position={'x': 10, 'y': 10})
        results.append("Clicked body after dateOfFormation")
        await page.select_option('#entityStateOfFormation', value=request.state_of_formation)
        results.append(f"Selected entityStateOfFormation with {request.state_of_formation}")
        await page.fill('#ENINo', value=request.ein_number)
        results.append(f"Filled ENINo with {request.ein_number}")
        await page.fill('#businessPhone', value=request.business_phone)
        results.append(f"Filled businessPhone with {request.business_phone}")
        await page.fill('#entityAddress', value=request.entity_address)
        results.append(f"Filled entityAddress with {request.entity_address}")
        await page.fill('#entityCity', value=request.entity_city)
        results.append(f"Filled entityCity with {request.entity_city}")
        await page.select_option('#entityState', value=request.entity_state)
        results.append(f"Selected entityState with {request.entity_state}")
        await page.fill('#entityZip', value=request.entity_zip)
        results.append(f"Filled entityZip with {request.entity_zip}")
        # ... (continue this pattern for all remaining actions)
        await browser.close()
    return results

@app.post("/run-actions")
async def run_actions(request: ActionRequest):
    results = await run_playwright_actions(request)
    return {"status": "success", "actions": results} 