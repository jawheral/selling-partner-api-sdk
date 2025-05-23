/**
 * Selling Partner API for Application Management
 * The Selling Partner API for Application Management lets you programmatically update the client secret on registered applications.
 *
 * The version of the OpenAPI document: 2023-11-30
 *
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import { ApiClient } from '../ApiClient.js'
import { ErrorList } from '../model/ErrorList.js'
import { SuperagentRateLimiter } from '../../../helper/SuperagentRateLimiter.mjs'
import { DefaultRateLimitFetcher } from '../../../helper/DefaultRateLimitFetcher.mjs'

/**
* Applications service.
* @module applications_v2023_11_30/api/ApplicationsApi
* @version 2023-11-30
*/
export class ApplicationsApi {
  // Private memeber stores the default rate limiters
  #defaultRateLimiterMap

  /**
    * Constructs a new ApplicationsApi.
    * @alias module:applications_v2023_11_30/api/ApplicationsApi
    * @class
    * @param {module:applications_v2023_11_30/ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:applications_v2023_11_30/ApiClient#instance} if unspecified.
    */
  constructor (apiClient) {
    this.apiClient = apiClient || ApiClient.instance
    this.initializeDefaultRateLimiterMap()
  }

  /**
     * Initialize rate limiters for API operations
     */
  initializeDefaultRateLimiterMap () {
    this.#defaultRateLimiterMap = new Map()
    const defaultRateLimitFetcher = new DefaultRateLimitFetcher()
    const operations = [
      'ApplicationsApi-rotateApplicationClientSecret'
    ]

    for (const operation of operations) {
      const config = defaultRateLimitFetcher.getLimit(operation)
      this.#defaultRateLimiterMap.set(operation, new SuperagentRateLimiter(config))
    }
  }

  /**
     * Get rate limiter for a specific operation
     * @param {String} operation name
     */
  getRateLimiter (operation) {
    return this.#defaultRateLimiterMap.get(operation)
  }

  /**
     * Rotates application client secrets for a developer application. Developers must register a destination queue in the developer console before calling this operation. When this operation is called a new client secret is generated and sent to the developer-registered queue. For more information, refer to [Rotate your application client secret](https://developer-docs.amazon.com/sp-api/v0/docs/application-management-api-v2023-11-30-use-case-guide#tutorial-rotate-your-applications-client-secret).  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.0167 | 1 |  The &#x60;x-amzn-RateLimit-Limit&#x60; response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
     * @return {Promise} a {@link https://www.promisejs.org/|Promise}, with an object containing HTTP response
     */
  rotateApplicationClientSecretWithHttpInfo () {
    const postBody = null

    const pathParams = {
    }
    const queryParams = {
    }
    const headerParams = {
    }
    const formParams = {
    }

    const contentTypes = []
    const accepts = ['application/json']
    const returnType = null

    return this.apiClient.callApi('ApplicationsApi-rotateApplicationClientSecret',
      '/applications/2023-11-30/clientSecret', 'POST',
      pathParams, queryParams, headerParams, formParams, postBody,
      contentTypes, accepts, returnType, this.getRateLimiter('ApplicationsApi-rotateApplicationClientSecret')
    )
  }

  /**
     * Rotates application client secrets for a developer application. Developers must register a destination queue in the developer console before calling this operation. When this operation is called a new client secret is generated and sent to the developer-registered queue. For more information, refer to [Rotate your application client secret](https://developer-docs.amazon.com/sp-api/v0/docs/application-management-api-v2023-11-30-use-case-guide#tutorial-rotate-your-applications-client-secret).  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.0167 | 1 |  The &#x60;x-amzn-RateLimit-Limit&#x60; response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values than those shown here. For more information, refer to [Usage Plans and Rate Limits in the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/usage-plans-and-rate-limits-in-the-sp-api).
     * @return {Promise} a {@link https://www.promisejs.org/|Promise}
     */
  rotateApplicationClientSecret () {
    return this.rotateApplicationClientSecretWithHttpInfo()
      .then(function (response_and_data) {
        return response_and_data.data
      })
  }
}
