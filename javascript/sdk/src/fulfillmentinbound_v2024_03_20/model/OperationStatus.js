/**
 * The Selling Partner API for FBA inbound operations.
 * The Selling Partner API for Fulfillment By Amazon (FBA) Inbound. The FBA Inbound API enables building inbound workflows to create, manage, and send shipments into Amazon's fulfillment network. The API has interoperability with the Send-to-Amazon user interface.
 *
 * The version of the OpenAPI document: 2024-03-20
 *
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import { ApiClient } from '../ApiClient.js'

/**
* Enum class OperationStatus.
* @enum {}
* @readonly
*/
export class OperationStatus {
  /**
         * value: "SUCCESS"
         * @const
         */
  'SUCCESS' = 'SUCCESS'

  /**
         * value: "FAILED"
         * @const
         */
  'FAILED' = 'FAILED'

  /**
         * value: "IN_PROGRESS"
         * @const
         */
  'IN_PROGRESS' = 'IN_PROGRESS'

  /**
    * Returns a <code>OperationStatus</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:fulfillmentinbound_v2024_03_20/model/OperationStatus} The enum <code>OperationStatus</code> value.
    */
  static constructFromObject (object) {
    return object
  }
}
