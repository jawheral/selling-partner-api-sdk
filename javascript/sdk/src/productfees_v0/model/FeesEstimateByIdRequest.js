/**
 * Selling Partner API for Product Fees
 * The Selling Partner API for Product Fees lets you programmatically retrieve estimated fees for a product. You can then account for those fees in your pricing.
 *
 * The version of the OpenAPI document: v0
 *
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import { ApiClient } from '../ApiClient.js'
import { FeesEstimateRequest } from './FeesEstimateRequest.js'
import { IdType } from './IdType.js'

/**
 * The FeesEstimateByIdRequest model module.
 * @module productfees_v0/model/FeesEstimateByIdRequest
 * @version v0
 */
export class FeesEstimateByIdRequest {
  /**
   * Constructs a new <code>FeesEstimateByIdRequest</code>.
   * A product, marketplace, and proposed price used to request estimated fees.
   * @alias module:productfees_v0/model/FeesEstimateByIdRequest
   * @class
   * @param idType {module:productfees_v0/model/IdType}
   * @param idValue {String} The item identifier.
   */
  constructor (idType, idValue) {
    this.idType = idType
    this.idValue = idValue
  }

  /**
   * Constructs a <code>FeesEstimateByIdRequest</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:productfees_v0/model/FeesEstimateByIdRequest} obj Optional instance to populate.
   * @return {module:productfees_v0/model/FeesEstimateByIdRequest} The populated <code>FeesEstimateByIdRequest</code> instance.
   */
  static constructFromObject (data, obj) {
    if (data) {
      switch (typeof data) {
        case 'string':
          obj = String(data)
          break
        case 'number':
          obj = Number(data)
          break
        case 'boolean':
          obj = Boolean(data)
          break
      }
      obj = obj || new FeesEstimateByIdRequest()
      if (data.hasOwnProperty('FeesEstimateRequest')) { obj.feesEstimateRequest = FeesEstimateRequest.constructFromObject(data.FeesEstimateRequest) }
      if (data.hasOwnProperty('IdType')) { obj.idType = IdType.constructFromObject(data.IdType) }
      if (data.hasOwnProperty('IdValue')) { obj.idValue = ApiClient.convertToType(data.IdValue, 'String') }
    }
    return obj
  }
}

/**
 * @member {module:productfees_v0/model/FeesEstimateRequest} feesEstimateRequest
 */
FeesEstimateByIdRequest.prototype.feesEstimateRequest = undefined

/**
 * @member {module:productfees_v0/model/IdType} idType
 */
FeesEstimateByIdRequest.prototype.idType = undefined

/**
 * The item identifier.
 * @member {String} idValue
 */
FeesEstimateByIdRequest.prototype.idValue = undefined
