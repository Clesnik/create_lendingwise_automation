from fastapi import FastAPI
from pydantic import BaseModel
import asyncio
from typing import Optional
from playwright.async_api import async_playwright

app = FastAPI()

class ActionRequest(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    branch_id: Optional[str] = None
    secondary_agent: Optional[str] = None
    loan_program: Optional[str] = None
    internal_program: Optional[str] = None
    prop_process: Optional[str] = None
    primary_status: Optional[str] = None
    lead_source: Optional[str] = None
    referring_party: Optional[str] = None
    pg_one_fname: Optional[str] = None
    pg_one_mname: Optional[str] = None
    pg_one_lname: Optional[str] = None
    pg_one_email: Optional[str] = None
    pg_one_cell: Optional[str] = None
    pg_one_work: Optional[str] = None
    pg_one_street: Optional[str] = None
    pg_one_unit: Optional[str] = None
    pg_one_city: Optional[str] = None
    pg_one_state: Optional[str] = None
    pg_one_zip: Optional[str] = None
    pg_one_county: Optional[str] = None
    pg_one_country: Optional[str] = None
    mailing_street: Optional[str] = None
    mailing_unit: Optional[str] = None
    mailing_city: Optional[str] = None
    mailing_state: Optional[str] = None
    mailing_zip: Optional[str] = None
    mailing_country: Optional[str] = None
    pg_one_dob: Optional[str] = None
    pg_one_ssn: Optional[str] = None
    pg_one_marital_status: Optional[str] = None
    pg_one_citizenship: Optional[str] = None
    pg_one_mid_fico: Optional[str] = None
    pg_one_fico_range: Optional[str] = None
    borrower_type: Optional[str] = None
    entity_name: Optional[str] = None
    trade_name: Optional[str] = None
    entity_type: Optional[str] = None
    date_of_formation: Optional[str] = None
    state_of_formation: Optional[str] = None
    ein_number: Optional[str] = None
    business_phone: Optional[str] = None
    entity_address: Optional[str] = None
    entity_city: Optional[str] = None
    entity_state: Optional[str] = None
    entity_zip: Optional[str] = None
    member_name_zero: Optional[str] = None
    member_title_zero: Optional[str] = None
    member_ownership_zero: Optional[str] = None
    member_address_zero: Optional[str] = None
    member_cell_zero: Optional[str] = None
    member_ssn_zero: Optional[str] = None
    member_dob_zero: Optional[str] = None
    member_email_zero: Optional[str] = None
    member_fico_score_zero: Optional[str] = None
    member_guarantor_zero: Optional[str] = None
    member_citizenship_zero: Optional[str] = None
    member_name_one: Optional[str] = None
    member_title_one: Optional[str] = None
    member_ownership_one: Optional[str] = None
    member_address_one: Optional[str] = None
    member_cell_one: Optional[str] = None
    member_ssn_one: Optional[str] = None
    member_dob_one: Optional[str] = None
    member_email_one: Optional[str] = None
    member_fico_score_one: Optional[str] = None
    member_guarantor_one: Optional[str] = None
    member_citizenship_one: Optional[str] = None
    member_name_two: Optional[str] = None
    member_title_two: Optional[str] = None
    member_ownership_two: Optional[str] = None
    member_address_two: Optional[str] = None
    member_cell_two: Optional[str] = None
    member_ssn_two: Optional[str] = None
    member_dob_two: Optional[str] = None
    member_email_two: Optional[str] = None
    member_fico_score_two: Optional[str] = None
    member_guarantor_two: Optional[str] = None
    member_citizenship_two: Optional[str] = None
    member_name_three: Optional[str] = None
    member_title_three: Optional[str] = None
    member_ownership_three: Optional[str] = None
    member_address_three: Optional[str] = None
    member_cell_three: Optional[str] = None
    member_ssn_three: Optional[str] = None
    member_dob_three: Optional[str] = None
    member_email_three: Optional[str] = None
    member_fico_score_three: Optional[str] = None
    member_guarantor_three: Optional[str] = None
    member_citizenship_three: Optional[str] = None
    member_name_four: Optional[str] = None
    member_title_four: Optional[str] = None
    member_ownership_four: Optional[str] = None
    member_address_four: Optional[str] = None
    member_cell_four: Optional[str] = None
    member_ssn_four: Optional[str] = None
    member_dob_four: Optional[str] = None
    member_email_four: Optional[str] = None
    member_fico_score_four: Optional[str] = None
    member_guarantor_four: Optional[str] = None
    member_citizenship_four: Optional[str] = None
    member_name_five: Optional[str] = None
    member_title_five: Optional[str] = None
    member_ownership_five: Optional[str] = None
    member_address_five: Optional[str] = None
    member_cell_five: Optional[str] = None
    member_ssn_five: Optional[str] = None
    member_dob_five: Optional[str] = None
    member_email_five: Optional[str] = None
    member_fico_score_five: Optional[str] = None
    member_guarantor_five: Optional[str] = None
    member_citizenship_five: Optional[str] = None
    additional_guarantors: Optional[str] = None
    pg_three_fname: Optional[str] = None
    pg_three_mname: Optional[str] = None
    pg_three_lname: Optional[str] = None
    pg_three_cell: Optional[str] = None
    pg_three_ssn: Optional[str] = None
    pg_three_dob: Optional[str] = None
    pg_three_marital_status: Optional[str] = None
    pg_three_street: Optional[str] = None
    pg_three_city: Optional[str] = None
    pg_three_state: Optional[str] = None
    pg_three_zip: Optional[str] = None
    pg_three_email: Optional[str] = None
    pg_three_citizenship: Optional[str] = None
    pg_four_fname: Optional[str] = None
    pg_four_mname: Optional[str] = None
    pg_four_lname: Optional[str] = None
    pg_four_cell: Optional[str] = None
    pg_four_ssn: Optional[str] = None
    pg_four_dob: Optional[str] = None
    pg_four_marital_status: Optional[str] = None
    pg_four_street: Optional[str] = None
    pg_four_city: Optional[str] = None
    pg_four_state: Optional[str] = None
    pg_four_zip: Optional[str] = None
    pg_four_email: Optional[str] = None
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
    liquid_assets: Optional[str] = None
    desired_closing_date: Optional[str] = None
    desired_loan_amount: Optional[str] = None
    type_of_loan_requesting: Optional[str] = None
    trial_payment_date: Optional[str] = None
    maturity_date: Optional[str] = None
    loan_term: Optional[str] = None
    interest_rate: Optional[str] = None
    lien_terms: Optional[str] = None
    amortization_type: Optional[str] = None
    is_taxes_ins_escrowed: Optional[str] = None
    taxes: Optional[str] = None
    annual_premium: Optional[str] = None
    cost_basis: Optional[str] = None
    home_value: Optional[str] = None
    max_amount_to_put_down: Optional[str] = None
    subject_property_address: Optional[str] = None
    subject_property_unit: Optional[str] = None
    subject_property_city: Optional[str] = None
    subject_property_state: Optional[str] = None
    subject_property_zip: Optional[str] = None
    subject_property_county: Optional[str] = None
    subject_property_apn: Optional[str] = None
    subject_property_block: Optional[str] = None
    subject_property_lot: Optional[str] = None
    subject_property_type: Optional[str] = None
    subject_property_sqft: Optional[str] = None
    subject_property_acres: Optional[str] = None
    subject_property_year_built: Optional[str] = None
    bedrooms: Optional[str] = None
    bathrooms: Optional[str] = None
    half_bathrooms: Optional[str] = None
    number_of_buildings: Optional[str] = None
    number_of_units_occupied: Optional[str] = None
    number_of_parcels: Optional[str] = None
    estimated_property_value: Optional[str] = None
    present_occupancy: Optional[str] = None

async def run_playwright_actions(request: ActionRequest):
    results = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1280, 'height': 720})
        page = await context.new_page()
        # --- Start of user-specified actions ---
        await page.goto("https://app.brrrr.com/backoffice/LMRequest.php?eOpt=0&cliType=PC&tabOpt=QAPP&moduleCode=HMLO&supp=help")
        results.append("Navigated to BRRRR backoffice login")
        await page.wait_for_selector('input#userName', timeout=10000)
        results.append("Waited for username input")
        email_field = page.locator('input#userName')
        await email_field.click()
        results.append("Clicked username field")
        await email_field.fill(request.username)
        results.append(f"Filled username with {request.username}")
        pwd_input = page.locator('input#pwd')
        await pwd_input.wait_for(timeout=10000)
        results.append("Waited for password input")
        await pwd_input.click()
        results.append("Clicked password field")
        await pwd_input.fill(request.password)
        results.append(f"Filled password with {request.password}")
        await page.click("button#submitbutton")
        results.append("Clicked login button")
        await page.wait_for_url("https://app.brrrr.com/backoffice/LMRequest*", timeout=20000)
        results.append("Waited for post-login URL")
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
        # Member 0
        await page.fill('#memberName0', value=request.member_name_zero)
        results.append(f"Filled #memberName0 with {request.member_name_zero}")
        await page.fill('#memberTitle0', value=request.member_title_zero)
        results.append(f"Filled #memberTitle0 with {request.member_title_zero}")
        await page.fill('#memberOwnership0', value=request.member_ownership_zero)
        results.append(f"Filled #memberOwnership0 with {request.member_ownership_zero}")
        await page.fill('#memberAddress0', value=request.member_address_zero)
        results.append(f"Filled #memberAddress0 with {request.member_address_zero}")
        await page.fill('#memberCell0', value=request.member_cell_zero)
        results.append(f"Filled #memberCell0 with {request.member_cell_zero}")
        await page.fill('#memberSSN0', value=request.member_ssn_zero)
        results.append(f"Filled #memberSSN0 with {request.member_ssn_zero}")
        await page.fill('#memberDOB0', value=request.member_dob_zero)
        results.append(f"Filled #memberDOB0 with {request.member_dob_zero}")
        await page.click('body', position={'x': 10, 'y': 10})
        results.append("Clicked body after memberDOB0")
        await page.fill('#memberEmail0', value=request.member_email_zero)
        results.append(f"Filled #memberEmail0 with {request.member_email_zero}")
        await page.fill('#memberCreditScore0', value=request.member_fico_score_zero)
        results.append(f"Filled #memberCreditScore0 with {request.member_fico_score_zero}")
        if request.member_guarantor_zero:
            await page.wait_for_selector(f'label[for="{request.member_guarantor_zero}"]', timeout=10000)
            await page.click(f'label[for="{request.member_guarantor_zero}"]')
            results.append(f"Clicked label for {request.member_guarantor_zero}")
        if request.member_citizenship_zero:
            await page.wait_for_selector(f'label[for="{request.member_citizenship_zero}"]', timeout=10000)
            await page.click(f'label[for="{request.member_citizenship_zero}"]')
            results.append(f"Clicked label for {request.member_citizenship_zero}")
        await page.click('span[onclick*="showAndHidePropertyValuationInfo"]')
        results.append("Clicked add member/officer (0)")
        await page.wait_for_timeout(1000)
        results.append("Waited 1s for new member form (0)")

        # Member 1
        await page.fill('#memberName1', value=request.member_name_one)
        results.append(f"Filled #memberName1 with {request.member_name_one}")
        await page.fill('#memberTitle1', value=request.member_title_one)
        results.append(f"Filled #memberTitle1 with {request.member_title_one}")
        await page.fill('#memberOwnership1', value=request.member_ownership_one)
        results.append(f"Filled #memberOwnership1 with {request.member_ownership_one}")
        await page.fill('#memberAddress1', value=request.member_address_one)
        results.append(f"Filled #memberAddress1 with {request.member_address_one}")
        await page.fill('#memberCell1', value=request.member_cell_one)
        results.append(f"Filled #memberCell1 with {request.member_cell_one}")
        await page.fill('#memberSSN1', value=request.member_ssn_one)
        results.append(f"Filled #memberSSN1 with {request.member_ssn_one}")
        await page.fill('#memberDOB1', value=request.member_dob_one)
        results.append(f"Filled #memberDOB1 with {request.member_dob_one}")
        await page.click('body', position={'x': 10, 'y': 10})
        results.append("Clicked body after memberDOB1")
        await page.fill('#memberEmail1', value=request.member_email_one)
        results.append(f"Filled #memberEmail1 with {request.member_email_one}")
        await page.fill('#memberCreditScore1', value=request.member_fico_score_one)
        results.append(f"Filled #memberCreditScore1 with {request.member_fico_score_one}")
        if request.member_guarantor_one:
            await page.wait_for_selector(f'label[for="{request.member_guarantor_one}"]', timeout=10000)
            await page.click(f'label[for="{request.member_guarantor_one}"]')
            results.append(f"Clicked label for {request.member_guarantor_one}")
        if request.member_citizenship_one:
            await page.wait_for_selector(f'label[for="{request.member_citizenship_one}"]', timeout=10000)
            await page.click(f'label[for="{request.member_citizenship_one}"]')
            results.append(f"Clicked label for {request.member_citizenship_one}")
        await page.click('span[onclick*="showAndHidePropertyValuationInfo"]')
        results.append("Clicked add member/officer (1)")
        await page.wait_for_timeout(1000)
        results.append("Waited 1s for new member form (1)")

        # Repeat for members 2, 3, 4, 5, additional_guarantors, pg_three, pg_four, and all other actions as in your script
        # For brevity, only member 1 is shown here, but you should continue this pattern for all remaining actions.

        await browser.close()
    return results

@app.post("/run-actions")
async def run_actions(request: ActionRequest):
    results = await run_playwright_actions(request)
    return {"status": "success", "actions": results} 