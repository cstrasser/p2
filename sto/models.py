from django.db import models

class Tblservicetask(models.Model):
    stid = models.SmallIntegerField(db_column='STID', primary_key=True)  # Field name made lowercase.
    stprojnum = models.CharField(db_column='STProjNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stentrydate = models.DateTimeField(db_column='STEntryDate')  # Field name made lowercase.
    ststatus = models.CharField(db_column='STStatus', max_length=15, blank=True, null=True)  # Field name made lowercase.
    stnotes = models.TextField(db_column='STNotes', blank=True, null=True)  # Field name made lowercase.
    strespperson = models.CharField(db_column='STRespPerson', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stbilling = models.CharField(db_column='STBilling', max_length=10)  # Field name made lowercase.
    sthotel = models.IntegerField(db_column='STHotel', blank=True, null=True)  # Field name made lowercase.
    stperdiem = models.IntegerField(db_column='STPerDiem', blank=True, null=True)  # Field name made lowercase.
    stmileage = models.IntegerField(db_column='STMileage', blank=True, null=True)  # Field name made lowercase.
    sttravel_hrs_field = models.IntegerField(db_column='STTravel(hrs)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    stsitework_hrs_field = models.IntegerField(db_column='STSiteWork(hrs)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ston_site_date = models.DateTimeField(db_column='STOn_Site_Date', blank=True, null=True)  # Field name made lowercase.
    sttech = models.CharField(db_column='STTech', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stbillingnotes = models.TextField(db_column='STBillingNotes', blank=True, null=True)  # Field name made lowercase.
    stinvoicenumber = models.CharField(db_column='STInvoiceNumber', max_length=15, blank=True, null=True)  # Field name made lowercase.
    oldstcustomer = models.CharField(db_column='OLDSTCustomer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    oldstcontact = models.CharField(db_column='OLDSTContact', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stbillingdate = models.DateTimeField(db_column='STBillingDate', blank=True, null=True)  # Field name made lowercase.
    stmaterials = models.DecimalField(db_column='STMaterials', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    stlabour = models.DecimalField(db_column='STLabour', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sttotal = models.DecimalField(db_column='STTotal', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    streference = models.CharField(db_column='STReference', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stphone = models.CharField(db_column='STPhone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stadd1 = models.CharField(db_column='STAdd1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stadd2 = models.CharField(db_column='STAdd2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stadd3 = models.CharField(db_column='STAdd3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stcity = models.CharField(db_column='STCity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ststate = models.CharField(db_column='STState', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stzip = models.CharField(db_column='STZip', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sttag = models.CharField(db_column='STTag', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stfedid = models.CharField(db_column='STFedID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stcell = models.CharField(db_column='STCell', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stemail = models.CharField(db_column='STEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stshipprior = models.CharField(db_column='STShipPrior', max_length=10, blank=True, null=True)  # Field name made lowercase.
    stshipcost = models.DecimalField(db_column='STShipCost', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    stshipmethod = models.CharField(db_column='STShipMethod', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sttechrate = models.DecimalField(db_column='STTechRate', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sttravrate = models.DecimalField(db_column='STTravRate', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    stmilerate = models.DecimalField(db_column='STMileRate', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    stperdeimrate = models.DecimalField(db_column='STPerDeimRate', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sthotelrate = models.DecimalField(db_column='STHotelRate', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    stactionreq = models.CharField(db_column='STActionReq', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stschdate = models.DateTimeField(db_column='STSchDate', blank=True, null=True)  # Field name made lowercase.
    stcountry = models.IntegerField(db_column='STCountry', blank=True, null=True)  # Field name made lowercase.
    stdescription = models.TextField(db_column='STDescription', blank=True, null=True)  # Field name made lowercase.
    stacknowledge = models.NullBooleanField(db_column='STAcknowledge')  # Field name made lowercase.
    stcustdesc = models.TextField(db_column='STCustDesc', blank=True, null=True)  # Field name made lowercase.
    stcustpo = models.CharField(db_column='STCustPO', max_length=34, blank=True, null=True)  # Field name made lowercase.
    stbillcoloc = models.IntegerField(db_column='STBillCoLoc', blank=True, null=True)  # Field name made lowercase.
    stbillcontact = models.IntegerField(db_column='STBillContact', blank=True, null=True)  # Field name made lowercase.
    stcustomer = models.IntegerField(db_column='STCustomer', blank=True, null=True)  # Field name made lowercase.
    stcontact = models.IntegerField(db_column='STContact', blank=True, null=True)  # Field name made lowercase.
    stproj_mgr = models.CharField(db_column='STProj_Mgr', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stpriority = models.CharField(db_column='STPriority', max_length=30, blank=True, null=True)  # Field name made lowercase.
    stclosedate = models.DateTimeField(db_column='STCloseDate', blank=True, null=True)  # Field name made lowercase.
    sttrackflag = models.NullBooleanField(db_column='STTrackFlag')  # Field name made lowercase.
    stcontact2 = models.IntegerField(db_column='STContact2', blank=True, null=True)  # Field name made lowercase.
    stcustomer2 = models.IntegerField(db_column='STCustomer2', blank=True, null=True)  # Field name made lowercase.
    strepcontact = models.IntegerField(db_column='STRepContact', blank=True, null=True)  # Field name made lowercase.
    stcurr = models.CharField(db_column='STCurr', max_length=3, blank=True, null=True)  # Field name made lowercase.
    st_type = models.CharField(db_column='ST_Type', max_length=15)  # Field name made lowercase.
    st_dla = models.DateTimeField(db_column='ST_DLA', blank=True, null=True)  # Field name made lowercase.
    st_days_att = models.IntegerField(db_column='ST_Days_Att', blank=True, null=True)  # Field name made lowercase.
    st_terms = models.CharField(db_column='ST_Terms', max_length=50, blank=True, null=True)  # Field name made lowercase.
    st_taxcode = models.CharField(db_column='ST_TAXCode', max_length=2, blank=True, null=True)  # Field name made lowercase.
    st_commrate = models.FloatField(db_column='ST_CommRate', blank=True, null=True)  # Field name made lowercase.
    stsalescomp = models.IntegerField(db_column='STSalesComp', blank=True, null=True)  # Field name made lowercase.
    st_tax1 = models.FloatField(db_column='ST_Tax1', blank=True, null=True)  # Field name made lowercase.
    st_tax2 = models.FloatField(db_column='ST_Tax2', blank=True, null=True)  # Field name made lowercase.
    st_county = models.CharField(db_column='ST_County', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stcommadder = models.FloatField(db_column='STCommAdder', blank=True, null=True)  # Field name made lowercase.
    st_account_type = models.CharField(db_column='ST_Account_Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    st_quote = models.CharField(db_column='ST_Quote', max_length=50, blank=True, null=True)  # Field name made lowercase.
    st_allposent = models.NullBooleanField(db_column='ST_AllPOSent')  # Field name made lowercase.
    st_segment = models.CharField(db_column='ST_Segment', max_length=50, blank=True, null=True)  # Field name made lowercase.
    st_site_type = models.CharField(db_column='ST_Site_Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    st_invoice_comment = models.CharField(db_column='ST_Invoice_Comment', max_length=100, blank=True, null=True)  # Field name made lowercase.
    st_def_gl = models.IntegerField(db_column='ST_Def_GL', blank=True, null=True)  # Field name made lowercase.
    st_def_dept = models.IntegerField(db_column='ST_Def_Dept', blank=True, null=True)  # Field name made lowercase.
    st_def_cogs_gl = models.IntegerField(db_column='ST_Def_COGS_GL', blank=True, null=True)  # Field name made lowercase.
    st_def_cogs_dept = models.IntegerField(db_column='ST_Def_COGS_Dept', blank=True, null=True)  # Field name made lowercase.
    stcompany = models.IntegerField(db_column='STCompany')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblServiceTask'
