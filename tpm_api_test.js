//constant uv's
import http from 'k6/http';
import { sleep, check } from 'k6';

const token='c44ef3ac177d4cfa2e160929ad2d37705c1db04f'

export default function() {
   const response1 = http.get('https://api-dev3.steeleglobal.net/rest/auditLogEvents', {
        headers: {
            'Authorization': `Bearer ${token}`, idptype: "keycloak" 
        }
    });
    check(response1, {
        'status is 200': (r) => r.status === 200,
    });
    console.log('Audit Log response is', response1.body);

    const response2 = http.get('https://api-dev3.steeleglobal.net/rest/case/billingUnitsPurchaseOrders', {
        headers: {
            'Authorization': `Bearer ${token}`, idptype: "keycloak" 
        }
    });
    check(response2, {
        'status is 200': (r) => r.status === 200,
    });
    console.log('Case Billing unit purchase order response is', response2.body);

    const response3 = http.get('https://api-dev3.steeleglobal.net/rest/case/folders?page=1&perPage=1000', {
        headers: {
            'Authorization': `Bearer ${token}`, idptype: "keycloak" 
        }
    });
    check(response3, {
        'status is 200': (r) => r.status === 200,
    });
    console.log('Case Folder response is', response3.body);

    const response4 = http.get('https://api-dev3.steeleglobal.net/rest/case/rejectionReasons', {
        headers: {
            'Authorization': `Bearer ${token}`, idptype: "keycloak" 
        }
    });
    check(response4, {
        'status is 200': (r) => r.status === 200,
    });
    console.log('Rejection reasons response is', response4.body);

    const response5 = http.get('https://api-dev3.steeleglobal.net/rest/case/scopes', {
        headers: {
            'Authorization': `Bearer ${token}`, idptype: "keycloak" 
        }
    });
    check(response5, {
        'status is 200': (r) => r.status === 200,
    });
    console.log(' Case scopes response is', response5.body);

    // const response6 = http.get('https://api-dev3.steeleglobal.net/rest/case/stages', {
    //     headers: {
    //         'Authorization': `Bearer ${token}`, idptype: "keycloak" 
    //     }
    // });
    // check(response6, {
    //     'status is 200': (r) => r.status === 200,
    // });
    // console.log('Case stages response is', response6.body);

    // const response7 = http.get('https://api-dev3.steeleglobal.net/rest/categories/caseReview', {
    //     headers: {
    //         'Authorization': `Bearer ${token}`, idptype: "keycloak" 
    //     }
    // });
    // check(response7, {
    //     'status is 200': (r) => r.status === 200,
    // });
    // console.log('Case Review response is', response7.body);

    // const response8 = http.get('https://api-dev3.steeleglobal.net/rest/categories/notes', {
    //     headers: {
    //         'Authorization': `Bearer ${token}`, idptype: "keycloak" 
    //     }
    // });
    // check(response8, {
    //     'status is 200': (r) => r.status === 200,
    // });
    // console.log('Notes response is', response8.body);

    // const response9 = http.get('https://api-dev3.steeleglobal.net/rest/countries', {
    //     headers: {
    //         'Authorization': `Bearer ${token}`, idptype: "keycloak" 
    //     }
    // });
    // check(response9, {
    //     'status is 200': (r) => r.status === 200,
    // });
    // console.log('Countries response is', response9.body);

    // const response10 = http.get('https://api-dev3.steeleglobal.net/rest/categories/userGates', {
    //     headers: {
    //         'Authorization': `Bearer ${token}`, idptype: "keycloak" 
    //     }
    // });
    // check(response10, {
    //     'status is 200': (r) => r.status === 200,
    // });
    // console.log('User gates response is', response10.body);

    
   sleep(1);
}



