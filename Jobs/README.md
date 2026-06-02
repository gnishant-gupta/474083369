## CA Close Ticket In CA For Closed Case
Sync closure of the tickets at the CA Desk Manager with Siemplify cases closure.


**Run Interval In Seconds:** 7200

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|API Root|String|True|http://x.x.x.x:<port>|
|Username|String|True|dfgh|
|Password|String|True|cgh|
|Group Filter|String|False|Tesght|
|Group Field|String|True|group.combo_name|
|Ticket Final Status|String|True|Closed|
|Script Name|String|True|TEST CLOSE|


readme## Google Chronicle Alerts Creator Job
This job will sync new SOAR alerts with Chronicle SIEM.
Note: This job is only supported from Chronicle SOAR version 6.2.30 and higher.


**Run Interval In Seconds:** 7200

#### Parameters
|Name|Type|Is Mandatory|Value|
|----|----|------------|-----|
|Environment|String|True|Default Environment|
|API Root|String|True|https://backstory.googleapis.com|
|User's Service Account|Password|False|*****|
|Workload Identity Email|Password|False|*****|
|Verify SSL|Boolean|False|true|


readme